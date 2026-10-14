# Modelo fiel a la planilla: ingreso(P,R) por cultivo
G={'gir':30.780834725989603,'mz':41.580834725989604,'soja':25.75}
crops={
 'Girasol AO':dict(R=2.6,P=450,C=975.7266667,inc=lambda P,R:0.98*R*(1.15*P-30.780834725989603+20)),
 'Girasol':   dict(R=2.6,P=450,C=972.71,     inc=lambda P,R:R*(1.13*P-30.780834725989603)),
 'Maíz':      dict(R=8.5,P=200,C=1152.01,    inc=lambda P,R:R*(P-41.580834725989604)),
 'Soja de 1ra':dict(R=2.8,P=355,C=862.1697,  inc=lambda P,R:R*(P-25.75)),
}
def solve(f,lo,hi):
    for _ in range(100):
        m=(lo+hi)/2
        if f(m)>0: hi=m
        else: lo=m
    return (lo+hi)/2
out={}
for n,c in crops.items():
    R,P,C,inc=c['R'],c['P'],c['C'],c['inc']
    I=inc(P,R); M=I-C; N=I/R
    RI=solve(lambda r:inc(P,r)-C,0,R*3)
    PD=solve(lambda p:inc(p,R)-C,0,P*3)
    grid=[[round(inc(P*(1+dp),R*(1+dr))-C) for dr in (-.2,-.1,0,.1,.2)] for dp in (.2,.1,0,-.1,-.2)]
    out[n]=dict(I=I,M=M,N=N,RI=RI,col=(R-RI)/R,sobra=R-RI,PD=PD,caida=(P-PD)/P,ret=M/C,colAct=M/I,grid=grid)
    print(f"{n}: I {I:.1f} M {M:.1f} N {N:.2f} RI {RI:.3f} col {100*(R-RI)/R:.1f}% sobra {1000*(R-RI):.0f}kg PD {PD:.1f} caida {100*(P-PD)/P:.1f}% ret {100*M/C:.1f}% colAct {100*M/I:.1f}%")
    for g in grid: print('   ',g)
