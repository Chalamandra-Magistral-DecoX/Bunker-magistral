import os

def get_metrics():
    try:
        with open('/home/chalamandramagistral/microcosmos_elite/data/metrics.log', 'r') as f:
            lines = f.readlines()[1:]
            if not lines: return 0.0, 45.0
            ctrs = [float(l.split(',')[3].split(':')[1]) for l in lines if 'CTR' in l]
            cpas = [float(l.split(',')[4].split(':')[1]) for l in lines if 'CPA' in l]
            avg_ctr = sum(ctrs) / len(ctrs) if ctrs else 0.5
            avg_cpa = sum(cpas) / len(cpas) if cpas else 45.0
            return avg_ctr, avg_cpa
    except: return 0.5, 45.0

ctr, cpa = get_metrics()
print(f"  ⚡ CTR: {ctr:.2f}% | 💸 CPA: ${cpa:.2f}")
print(f"  📈 ROAS: {(1200/cpa if cpa > 0 else 0):.1f}x | LTV: $1,200")
