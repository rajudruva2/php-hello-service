import argparse,csv
from pathlib import Path
from datetime import date
F=Path("expenses.csv")
def main():
 p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True)
 a=s.add_parser("add"); a.add_argument("amount",type=float); a.add_argument("category"); a.add_argument("--note",default="")
 s.add_parser("total"); x=p.parse_args()
 if x.cmd=="add":
  if x.amount<=0:p.error("amount must be positive")
  new=not F.exists()
  with F.open("a",newline="",encoding="utf-8") as f:
   w=csv.writer(f)
   if new:w.writerow(["date","amount","category","note"])
   w.writerow([date.today().isoformat(),x.amount,x.category,x.note])
  print("Expense saved")
 else:
  with F.open(newline="",encoding="utf-8") as f: print("Total:",sum(float(r["amount"]) for r in csv.DictReader(f))) if F.exists() else print("Total: 0")
if __name__=="__main__":main()
