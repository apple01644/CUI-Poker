from random import shuffle, randint
from time import sleep

def n2c(n):
    if n == 1:
        return 'A'
    elif n == 10:
        return 'T'
    elif n == 11:
        return 'J'
    elif n == 12:
        return 'Q'
    elif n == 13:
        return 'K'
    else:
        return str(n)
    
class user:
    def __init__(self, name):
        self.name = name
        self.chip = 10 + randint(0, 20)
        self.deal = 0
        self.hand = []
        self.shown = []
        self.ai = True
        self.live = True
    def __repr__(self):
        if self.isLive():
            s = 'Live-'
        else:
            s = 'Died-'
        s += str(self.chip)
class card:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def __repr__(self):
        return self.m + n2c(self.n)
        
def take_card():
    o = deck[0]
    del deck[0]
    return o
def show_card(u, n):
    u.shown.append(n)
    

def round_table(table, d=0):
    print('---===---round table---===---')
    deal = 0
    if d != 0:
    	deal = d
    for u in users:
    	u.deal = -1
    i = 0
    r = 1
    while True:
    	u = users[i]
    	if u.chip > 0 and u.live:
    		#0:call 1:raise 2:die 3:all in
    		s = 2
    		if u.deal == deal:
    			break
    		if u.ai:
    			print(u.name)
    			sleep(1)
    			if u.chip <= deal - u.deal and u.deal > 0 or u.deal <= 0 and u.chip <= deal:
    				if randint(0, 2 + deal - u.chip) != 0:
    					s = 3
    			else:
    				v = int(valuing(u.hand))
    				
    				if v  + randint(0, 4) +randint(0, 4)  >= 10 + r * 1.5 and (u.chip >= deal - u.deal + r and u.deal > 0 or u.chip >= deal + r and u.deal <= 0) and d == 0:
    					s = 1
    				elif v + randint(0, 3) + randint(0, 4) >= 3 + r  * 1.5:
    					s = 0
    		else:
    			#player do
    			sec = ['Call', 'Die']
    			
    			if u.chip <= deal - u.deal and u.deal > 0 or u.deal <= 0 and u.chip <= deal:
    				sec[0] = 'All in'
    			else:
    				if deal == 0:
    					sec[0] = 'Check'
    				if (u.chip >= deal - u.deal + r and u.deal > 0 or u.chip >= deal + r and u.deal <= 0) and d == 0:
    					sec.append('Raise')
    			print(sec, 'Your chips', u.chip, ',Now deal', deal)
    			print(u.hand)
    			s = sec[int(input('select>')) - 1]
    			if s == 'All in':
    				s = 3
    			elif s == 'Call' or s == 'Check':
    				s =0
    			elif s == 'Raise':
    				s = 1
    			else:
    				s = 2
    			 
    			
    		if s == 0:
    			if deal == 0:
    				print('ⓒheck')
    				u.deal = 0
    			else:
    				print( 'ⓒall', deal)
    				if u.deal < 0:
    					u.deal = 0
    				table += deal - u.deal
    				u.chip -= deal - u.deal
    				u.deal = deal
    		elif s == 1:
    			print('ⓡaise to', deal + r)
    			deal += r
    			r += 1
    			if u.deal < 0:
    				u.deal = 0
    			table += deal - u.deal
    			u.chip -= deal - u.deal
    			u.deal = deal
    		elif s == 2:
    			print('ⓓie')
    			u.live = False
    		else:
    			print('ⓐll in')
    			table += u.chip
    			u.chip = 0
    		if u.ai:
    			sleep(2)
    			
    				
    	loop = True
    	for user in users:
    		if user.chip > 0 and user.live:
    			loop = False
    			break
    	if loop:
    		break
    	i = (i + 1) % len(users)
    shuffle(users)
    return table
    		
    
def admin_print(s=None, s1=None):
    pass
def m2s(m):
    if m == '♥':
        return 0.25
    elif m == '◆':
        return 0.5
    elif m == '♠':
        return 0.75
    elif m == '♣':
        return 0.0
    
def valuing(bundle):
    #0:None, 1:Straight, 2:Back-Straight, 3:Mountain
    line_state = 0    
    is_Flush = True
    v = 0
    have = []
    for _ in range(0, 14):
        have.append(0)
        
    for c in bundle:
        have[c.n] += 1
    
    if len(bundle) == 5:
        #is straight?
        for s in range(2,10):
            seq = True
            for d in range(0,5):
                if have[s + d] == 0:
                    seq = False
                    break
            if seq:
                line_state = 1
        #is back-staringht?
        seq = True
        for d in range(0,5):
            if have[1 + d] == 0:
                seq = False
                break
        if seq:
            line_state = 2

        #is mountain?
        if have[1] == 1 and have[10] == 1 and have[11] == 1 and have[12] == 1 and have[13] == 1:
            line_state = 3

        s = bundle[0].m
        for _ in range(1,5):
            if bundle[_].m == s:
                s = bundle[_].m
            else:
                is_Flush = False
                break

    

    pair = 0
    triple = 0
    four = 0
    for _ in range(1, 14):
        if have[_] == 2:
            pair += 1
        elif have[_] == 3:
            triple += 1
        elif have[_] == 4:
            four += 1

    
    if is_Flush:
        if line_state == 3:
            return 12 + m2s(bundle[0].m)
        elif line_state == 2:
            return 11 + m2s(bundle[0].m)
        elif line_state == 1:
            for _ in range(1, 14):
                if have[_] > 0:
                    mn = _
                    break
            return 10 + (mn + m2s(bundle[0].m)) / 14
    if four > 0:
        for _ in range(1, 14):
            if have[_] == 4:
                mn = _
                break
        return 9 + mn / 14
    if triple > 0 and pair > 0:
        for _ in range(1, 14):
            if have[_] == 3:
                mn = _
                break
        return 8 + mn / 14
    if is_Flush:
        for _ in range(1, 14):
            if have[_] > 0:
                mn = _
        return 7 + mn / 14
    if line_state == 3:
        return 6 + m2s(bundle[0].m)
    elif line_state == 2:
        return 5 + m2s(bundle[0].m)
    elif line_state == 1:
        for _ in range(1, 14):
            if have[_] > 0:
                mn = _
                break
        return 4 + (mn + m2s(bundle[0].m)) / 14
    if triple > 0:
        for _ in range(1, 14):
            if have[_] == 3:
                mk = 0
                for c in bundle:
                    v = m2s(c.m)
                    if c.n == _ and v > mk:
                        mk = v
                mn = _
                break
        return 3 + (mn + mk) / 14
    if pair > 1:
        for _ in range(1, 14):
            if have[_] == 2:
                mk = 0
                for c in bundle:
                    v = m2s(c.m)
                    if c.n == _ and v > mk:
                        mk = v
                mn = _
        return 2 + (mn + mk) / 14
    if pair > 0:
        for _ in range(1, 14):
            if have[_] == 2:
                mk = 0
                for c in bundle:
                    v = m2s(c.m)
                    if c.n == _ and v > mk:
                        mk = v
                mn = _
        return 1 + (mn + mk) / 14
    mk = 0
    for c in bundle:
        v = m2s(c.m)
        if c.n == _ and v > mk:
            mk = v
    for _ in range(1, 14):
        if have[_] == 1:
            mn = _
    return (mn + mk) / 14
    
def v2w(v):
    if v >= 13:
        return 'Overflow'
    if v >= 12:
        return 'Loyal Strainght FLush'
    if v >= 11:
        return 'Back-Straight Flush'
    if v >= 10:
        return 'Straight Flush'
    if v >= 9:
        return 'Four cards'
    if v >= 8:
        return 'Full house'
    if v >= 7:
        return 'Flush'
    if v >= 6:
        return 'Mountain'
    if v >= 5:
        return 'Back-Straight'
    if v >= 4:
        return 'Straight'
    if v >= 3:
        return 'Triple'
    if v >= 2:
        return 'Two pair'
    if v >= 1:
        return 'A pair'
    elif v >= 0:
        return 'Top'
    else:
        return 'Underflow'

#init user
deck = []
users = []
for name in ['Knight','Queen','Bishorp','Rock', 'King', 'Pone']:
    users.append(user(name))
users[0].ai = False

while True:

    #game start
    deck = []
    for m in ['♥','◆','♠','♣']:
        for n in range(1, 14):
            deck.append(card(m, n))
    shuffle(deck)
    table = 0

    #in game
    
    print('---===---give four cards---===---')
    for time in range(4):
        for user in users:
            if user.live:
                c = take_card()
                user.hand.append(c)
                if not user.ai:
                    print('!you get', c)
                admin_print('%-9s'%user.name, user.hand)

    print('---===---throw one hiden card---===---')
    for user in users:
        if user.live:
            if user.ai:
                pick = randint(0,len(user.hand) - 1)
            else:
                print('your hand', user.hand)
                pick = int(input('throw one card>')) - 1
            admin_print('throw', user.hand[pick])
            del user.hand[pick]

    print('---===---show the card---===---')
    for user in users:
        if user.live:
            if user.ai:
            	print('%-9s\'s shown'%user.name)
            	sleep(1)
            	pick = randint(0,len(user.hand) - 1)
            	print('>' + str(user.hand[pick]))
            	sleep(2)
            else:
                print('your hand', user.hand)
                pick = int(input('show one card>')) - 1
            admin_print('show', user.hand[pick])
            show_card(user, user.hand[pick])

    table = round_table(table, 1)
    
    print('---===---give one cards---===---')
    for user in users:
        if user.live:
            c = take_card()
            show_card(user, c)
            user.hand.append(c)
            if not user.ai:
                print('!you get', c)
            else:
             	print('%-9s'%user.name, user.shown)
                
    table = round_table(table)
    i = 0
    print('---===---give two cards---===---')
    for time in range(2):
        for user in users:
            if user.live:
                c = take_card()
                show_card(user, c)
                user.hand.append(c)
                if not user.ai:
                    print('!you get', c)
                else:
                    print('%-9s'%user.name, user.shown)
        if i == 0:
            i = 1
            print('------------------')
        
    table = round_table(table)
    
    print('---===---give one cards---===---')
    for user in users:
        if user.live:
            c = take_card()
            user.hand.append(c)
            if not user.ai:
                print('!you get', c)
            
    table = round_table(table)

    print('---===---throw two cards---===---')
    for user in users:
        if user.live:
            for time in range(2):
                if user.ai:
                    pick = randint(0,len(user.hand) - 1)
                else:
                    print('your hand', user.hand)
                    pick = int(input('throw one card>')) - 1
                admin_print('throw', user.hand[pick])
                del user.hand[pick]
                

    print('---===---final act---===---')
    o = {'p':-1, 'i':-1}
    i = 0
    for user in users:
        if len(user.hand) > 0:
            v = valuing(user.hand)
            if v > o['p'] and user.live:
                o['p'] = v
                o['i'] = i
            i += 1
    i = 0
    for user in users:
        if len(user.hand) > 0:
            v = valuing(user.hand)
            sleep(2)
            if user.ai:
                if i == o['i']:
                    print('%-9s'%user.name,user.hand, v2w(v), '☆', user.chip, '+', table)
                else:
                    if user.live:
                        print('%-9s'%user.name, user.hand, v2w(v), user.chip)
                    else:
                        print('%-9s'%user.name,user.hand, 'died', user.chip)
            else:
                if i == o['i']:
                    print('%-9s'%user.name,user.hand, v2w(v),'you', '☆',user.chip,'+', table)
                else: 
                    if user.live:
                        print('%-9s'%user.name,user.hand, v2w(v), 'you', user.chip)
                    else:
                        print('%-9s'%user.name,user.hand, 'died you', user.chip)
            if i == o['i']:
                user.chip += table
            i += 1
    

    input('---===---end---===---')

    #game end
        
    undie = 0
    for user in users:
        user.hand = []
        user.shown = []
        if user.chip == 0:
            user.live = False
        else:
            undie += 1
            user.live = True
    if undie <= 1:
        break

