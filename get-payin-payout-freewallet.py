import time

no = str(input('Digite o nome do arquivo: '))
aq = open('{}.txt'.format(no),'r')
tex = aq.readlines()
t = []
l = []
for inf in tex:
    m = inf.split('{')
    for i in m:
        for j in i.split('}'):
            for n in j.split(','):
                o = n.split(':')
                msg = str(o[0].replace('"',''))
                if (msg == 'currency' or msg == 'hash' or msg == 'payoutAddress' or msg == 'amount' or msg == 'type' or msg == 'recipient_address'):
                    if(o[1] != '"data"' and o[1] != '"fwh_etht"'): 
                    	t.append(o[0])
                    	l.append(o[1])

n = 0
tk = 0
currency = []
hash1 = []
tipe = []
amount = []
ra = []

for hj in t:
    if(hj == '"currency"' and n == 0):
        msg = l[tk]
        currency.append(msg)
    if(hj != '"currency"' and n == 0):
        n = 5
    if(hj == '"hash"' and n == 1):
        msg = l[tk]
        hash1.append(msg)
    if(hj != '"hash"' and n == 1):
        currency.pop()
        n = 5
    if(hj == '"amount"' and n == 2):
        msg = l[tk]
        amount.append(msg)
    if(hj != '"amount"' and n == 2):
        currency.pop()
        hash1.pop()
        n = 5
    if(hj == '"type"' and n == 3):
        msg = l[tk]
        tipe.append(msg)
    if(hj != '"type"' and n == 3):
        currency.pop()
        hash1.pop()
        amount.pop()
        n = 5
    if(hj == '"recipient_address"' and n == 4):
        msg = l[tk]
        ra.append(msg)
    if(hj != '"recipient_address"' and n == 4):
        currency.pop()
        hash1.pop()
        amount.pop()
        tipe.pop()
        n = 0
    if(n < 4):
    	n = n + 1
    	tk = tk + 1
    else:
    	n = 0
    	tk = tk + 1
	
tam = len(currency)
a = 0
tx=''
while (a < tam):
	tx += currency[a] + "," + hash1[a] + "," + amount[a] + "," + tipe[a] + "," + ra[a] + "\n"
	a += 1

filename=open("/home/ubuntu/script-py/freewallet-payin-payout", "w")
filename.write(tx)

n = 0
tk = 0
currency = []
hash1 = []
tipe = []
amount = []
pa = []

for hj in t:
    if(hj == '"currency"' and n == 0):
        msg = l[tk]
        currency.append(msg)
    if(hj != '"currency"' and n == 0):
        n = 5
    if(hj == '"hash"' and n == 1):
        msg = l[tk]
        hash1.append(msg)
    if(hj != '"hash"' and n == 1):
        currency.pop()
        n = 5
    if(hj == '"payoutAddress"' and n == 2):
        msg = l[tk]
        pa.append(msg)
    if(hj != '"payoutAddress"' and n == 2):
        currency.pop()
        hash1.pop()
        n = 5
    if(hj == '"amount"' and n == 3):
        msg = l[tk]
       	amount.append(msg)
    if(hj != '"amount"' and n == 3):
        currency.pop()
        hash1.pop()
        pa.pop()
        n = 5
    if(hj == '"type"' and n == 4):
        msg = l[tk]
        tipe.append(msg)
    if(hj != '"type"' and n == 4):
        currency.pop()
        hash1.pop()
        pa.pop()
        amount.pop()	
        n = 0
    if(n < 4):
        n = n + 1
        tk = tk + 1
    else:
        n = 0
        tk = tk + 1

tam = len(currency)
a = 0
while (a < tam):
        tx += currency[a] + "," + hash1[a] + "," + amount[a] + "," + tipe[a] + "," + pa[a] + "\n"
        a += 1

filename=open("/home/ubuntu/script-py/freewallet-payin-payout", "w")
filename.write(tx)

