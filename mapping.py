x=(2,3,4,5,6)
y=list(map(lambda i:i*i,x))
print(y)
print(x)

inr = [829, 867, 7356, 525]
usd = list(map(lambda i: f"{i / 75:.2f}", inr))
print(usd)

inr2 = [(21, "jn", 23223), (32, "ef", 565), (42, "grg", 874), (87, "ujh", 984)]
usd2 = lambda inr2: (inr2[0], inr2[1], f"{inr2[2] / 75:.2f}")
usd3 = lambda inr2: (inr2[1], f"{inr2[2] / 75:.2f}")

inr2_usd = list(map(usd2, inr2))
inr3_usd = list(map(usd3, inr2))

print(inr2_usd)
print(inr3_usd)

def odd_even(num):
    if num%2 ==0:
        return "even"
    else:
        return "odd"
nums=[79,87,4546,87,58]
lemme =list(map(odd_even,nums))
print(lemme)

n1= [1000,200,397,979,878]
fn= lambda i:i<500
final=list(filter(fn,n1))
print(final)
strn = [("naveen",21),("deva",22),("deepak",23)]
test=list(filter(lambda i:i[0][0]=='d',strn))
print(test)

#reduce
import functools
ss=[1,2,3,4,5]
ss_sum= functools.reduce(lambda i,j :i+j,ss)
print(ss_sum)
sc=['n','a','v']
sc_add=functools.reduce(lambda i,j :i+" "+j+"",sc)
print(sc_add)