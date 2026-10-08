"""Conservative pattern screen. Reports locations and counts, never matched values."""
import argparse,base64,json,pathlib,re,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
PATTERNS={
 'credential':re.compile(r'(?:sk-(?:ant-|or-v1-)?[A-Za-z0-9_-]{24,}|gh[pousr]_[A-Za-z0-9]{20,}|pypi-[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16})'),
 'private_key':re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
 'email':re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
 'phone':re.compile(r'(?<!\d)(?:\+1[ .-]?)?\([2-9]\d{2}\)[ .-]?\d{3}[ .-]\d{4}(?!\d)'),
 'local_home_path':re.compile(r'/(?:Users|home)/[A-Za-z0-9_.-]+/'),
}
def hits(text,label):
 return [{'location':label,'type':k,'matches':len(rx.findall(text))} for k,rx in PATTERNS.items() if rx.search(text)]
def scan_public():
 findings=[];files=0
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or any(x in {'.git','__pycache__'} for x in p.relative_to(ROOT).parts):continue
  files+=1;findings.extend(hits(p.read_text(encoding='utf-8'),str(p.relative_to(ROOT))))
 return files,findings
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--archive',type=pathlib.Path);args=ap.parse_args()
 files,findings=scan_public();original=[];count=0
 if args.archive:
  with zipfile.ZipFile(args.archive) as z:
   for item in __import__('csv').DictReader((ROOT/'data/attempts.csv').open()):
    d=json.loads(z.read(item['raw_member']));tr=d['transport']
    # Decode base64 to avoid overlooking secrets in retained response bodies.
    text=base64.b64decode(tr['raw_body_base64']).decode('utf-8',errors='replace')
    text+='\n'+json.dumps(d['request']['body'],ensure_ascii=False)
    original.extend(hits(text,item['attempt_id']));count+=1
 print(json.dumps({'public_files_scanned':files,'public_findings':findings,'original_attempt_bodies_scanned':count,'original_findings':original,'scope':'Pattern screen, not exhaustive personal-information detection. Full response bodies and reasoning are included; original HTTP/request headers are not.'},indent=2))
 if findings:raise SystemExit(1)
if __name__=='__main__':main()
