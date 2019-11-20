import random
from pip._vendor.distlib.compat import raw_input
from scipy import stats

# Arda Sonmez 041501003
# Aytac Aydemir 041402015

game=True
while game==True:
    print()
    ant = int(raw_input('Game Type: (1) human, (2) random player, (3) rule-based player,(4) statistical-rule learner,' 
    '(5) statistical-decider, (0)Exit'))
    ###############################################
    if ant==1:
        print("human vs human")
        P1_Score = 0
        P2_Score = 0
        d_Score = 0
        a_way = False
        while a_way==False:
            a = int(raw_input('Player1= Make Your Choice: 1=Rock, 2=Paper, 3=Scissors 0=Finish'))

            if a == 1:
                print("Player1= Rock")
            elif a == 2:
                print("Player1= Paper")
            elif a == 3:
                print("Player1= Scissors")
            elif a == 0:
                print("Escaped")
                break

            b = int(raw_input('Player2= Make Your Choice: 1=Rock, 2=Paper, 3=Scissors 0=Finish'))

            sum = a + b
            if b == 1:
                print("Rock")
            elif b == 2:
                print("Paper")
            elif b == 3:
                print("Scissors")
            elif b == 0:
                print("Escaped")
                break


            if b == a:
                print("draw")
                d_Score += 1
            elif b != a:
                # print("not raw")
                if sum == 3:
                    if a == 2:
                        print("P1 Win")

                        P1_Score += 1
                    else:
                        print("P2 Win")
                        P2_Score += 1
                if sum == 4:
                    if a == 1:
                        print("P1 Win")

                        P1_Score += 1
                    else:
                        print("P2 Win")
                        P2_Score+= 1
            if sum == 5:
                if a == 3:
                    print("P1 Win")

                    P1_Score += 1

                else:
                    print("P2 Win")
                    P2_Score += 1
        print("human vs human")
        print("P1 Score=", P1_Score)
        print("Tie Score=", d_Score)
        print("P2 Score=", P2_Score)
    ###############################################
    elif ant==2:
            print("human vs computer")

            w_Score = 0  # number of wins
            l_Score = 0  # number of loses
            d_Score = 0  # number of draws
            c = 0

            a_way = False

            while a_way == False:



                a = int(raw_input('Make Your Choice: 1=Rock, 2=Paper, 3=Scissors 0=Exit'))

                if a == 1:
                    print("Rock")
                elif a == 2:
                    print("Paper")
                elif a == 3:
                    print("Scissors")
                elif a == 0:
                    a_way = True

                # random choice by computer
                b = random.randrange(1, 4, 1)







                # we checked which 2 elements choosen
                sum = a + b
                if b == 1:
                    print("Rock")
                elif b == 2:
                    print("Paper")
                elif b == 3:
                    print("Scissors")

                # if both of choices are same, its draw!
                if b == a:
                    print("draw")

                    d_Score += 1


                elif b != a:
                # print("not raw")
                # if chosen elements are paper and rock
                    if sum == 3:
                        if a == 2:
                            print("You Win")

                            c = b
                            w_Score += 1
                        else:
                            print("You Lose")


                            l_Score += 1

                # if chosen elements are rock and scissor
                    if sum == 4:
                        if a == 1:
                            print("You Win")

                            c = b
                            w_Score += 1

                        else:
                            print("You Lose")


                            l_Score += 1

                    # if chosen elements are paper and scissor
                    if sum == 5:
                        if a == 3:
                            print("You Win")

                            c = b
                            w_Score += 1
                        else:
                            print("You Lose")
                            l_Score += 1

    # final scores for win,lose and tie
            print("your Score=", w_Score)
            print("your tie Score=", d_Score)
            print("Computer Score=", l_Score)
    ###############################################
    elif ant==3:
        print("human vs rules")
        w_Score = 0
        l_Score = 0
        d_Score = 0
        c = 0
        game = True
        a_way = False
        while game == True:
            a = int(raw_input('Make Your Choice: 0=Finish 1=Rock, 2=Paper, 3=Scissors'))
            if a == 1:
                print("Rock")
            elif a == 2:
                print("Paper")
            elif a == 3:
                print("Scissors")
            elif a == 0:
                break

            b = random.randrange(1, 4, 1)
            if a_way == True:
                while b == c or b == a:
                    b = random.randrange(1, 4, 1)
            # print(b)
            sum = a + b
            if b == 1:
                print("Rock")
            elif b == 2:
                print("Paper")
            elif b == 3:
                print("Scissors")

            if b == a:
                print("draw")
                print("*********************")
                a_way = False
                d_Score += 1
            elif b != a:
                # print("not raw")
                if sum == 3:
                    if a == 2:
                        print("You Win")
                        print("*********************")
                        a_way = True
                        c = b
                        w_Score += 1
                    else:
                        print("You Lose")
                        print("*********************")
                        a_way = False

                        l_Score += 1

                if sum == 4:
                    if a == 1:
                        print("You Win")
                        a_way = True
                        c = b
                        w_Score += 1

                    else:
                        print("You Lose")
                        a_way = False

                        l_Score += 1
            if sum == 5:
                if a == 3:
                    print("You Win")
                    a_way = True
                    c = b
                    w_Score += 1

                else:
                    print("You Lose")
                    a_way = False

                    l_Score += 1
        print("your Score=", w_Score)
        print("your tie Score=", d_Score)
        print("Computer Score=", l_Score)
    ###############################################
    elif ant == 4:
        print("static decider")
        w_Score = 0
        l_Score = 0
        d_Score = 0
        c = 0
        i = 0
        j = 0
        k = 0
        t = 0
        gamer = True
        a_way = False
        while gamer == True:
            a = int(raw_input('Make Your Choice:  1=Rock, 2=Paper, 3=Scissors, 0=Finish'))
            if a == 1:
                print("Rock")
                t = t + 1
                i = i + 1
                print("probability of user's Rock choose is %=", 100 * i / (i + j + k))

            elif a == 2:
                t = t + 1
                print("Paper")
                j = j + 1
                print("probability of user's Paper choose is %=", 100 * j / (i + j + k))
            elif a == 3:
                t = t + 1
                print("Scissors")
                k = k + 1
                print("probability of user's Scissor choose is %=", 100 * k / (i + j + k))
            elif a == 0:
                gamer = False

            if t == 1:
                b = random.randrange(1, 4, 1)
            elif t > 1:
                if (i > j and i > k):
                    print("contra of the highest probability of user's choose is paper,computer is choosing paper")
                    b = 2
                elif (j > k and j > i):
                    print("contra of the highest probability of user's choose is scissor,computer is choosing scissor")
                    b = 3
                elif (k > i and k > j):
                    print("contra of the highest probability of user's choose is rock,computer is choosing rock")
                    b = 1
                elif (j == k and j > i):
                    b = 2
                elif (i == j and i > k):
                    b = 1
                elif (i == k and k > j):
                    b = 3
            # print(b)
            sum = a + b
            if b == 1:
                print("Rock")
            elif b == 2:
                print("Paper")
            elif b == 3:
                print("Scissors")

            if b == a:
                print("draw")
                print("*********************")

                d_Score += 1
            elif b != a:
                # print("not raw")
                if sum == 3:
                    if a == 2:
                        print("You Win")
                        print("*********************")

                        c = b
                        w_Score += 1
                    else:
                        print("You Lose")
                        print("*********************")

                        l_Score += 1

                if sum == 4:
                    if a == 1:
                        print("You Win")

                        c = b
                        w_Score += 1

                    else:
                        print("You Lose")

                        l_Score += 1
            if sum == 5:
                if a == 3:
                    print("You Win")

                    c = b
                    w_Score += 1

                else:
                    print("You Lose")

                    l_Score += 1
        print("your Score=", w_Score)
        print("your tie Score=", d_Score)
        print("Computer Score=", l_Score)

    ###############################################
    elif ant==5:
            print("static decider")
            List = []
            w_Score = 0
            l_Score = 0
            d_Score = 0
            c = 0
            g = 0
            a_way = False
            rr = 0
            rp = 0
            rs = 0
            pr = 0
            ps = 0
            pp = 0
            ss = 0
            sp = 0
            sr = 0
            rrp = 0
            rpr = 0
            rsr = 0
            prr = 0
            psr = 0
            ppr = 0
            ssr = 0
            spr = 0
            srr = 0
            rrs = 0
            rpp = 0
            rsp = 0
            prp = 0
            psp = 0
            ppp = 0
            ssp = 0
            spp = 0
            srp = 0
            rrr = 0
            rps = 0
            rss = 0
            prs = 0
            pss = 0
            pps = 0
            sss = 0
            sps = 0
            srs = 0

            triRRR = 0
            triRRS = 0
            triRRP = 0
            triRPS = 0
            triRPP = 0
            triRPR = 0
            triRSS = 0
            triRSP = 0
            triRSR = 0
            triPRS = 0
            triPRP = 0
            triPRR = 0
            triPSS = 0
            triPSP = 0
            triPSR = 0
            triPPS = 0
            triPPP = 0
            triPPR = 0
            triSSP = 0
            triSSR = 0
            triSPS = 0
            triSPP = 0
            triSPR = 0
            triSRS = 0
            triSRP = 0
            triSRR = 0
            triSSS = 0
            tsk5 = True

            while tsk5 == True:
                a = int(raw_input('Make Your Choice: 1=Rock, 2=Paper, 3=Scissors 0=Exit'))
                # a = random.randrange(1, 4, 1)
                List.append(a)
                if a == 1:
                    print("Rock")
                elif a == 2:
                    print("Paper")
                elif a == 3:
                    print("Scissors")
                elif a == 0:
                    print("One more? :)")
                    break
                if g < 3:
                    b = random.randrange(1, 4, 1)
                    g = g + 1
                elif g >= 3:

                    if List[len(List) - 3] == 1:  # r _ _
                        if List[len(List) - 2] == 1:  # r r _
                            rr = rr + 1
                            if List[len(List) - 1] == 1:  # r r r
                                rrr = rrr + 1
                            elif List[len(List) - 1] == 2:  # r r p
                                rrp = rrp + 1
                            elif List[len(List) - 1] == 3:  # r r s
                                rrs = rrs + 1

                        elif List[len(List) - 2] == 2:  # r p _
                            rp = rp + 1
                            if List[len(List) - 1] == 1:  # r p r
                                rpr = rpr + 1
                            elif List[len(List) - 1] == 2:  # r p p
                                rpp = rpp + 1
                            elif List[len(List) - 1] == 3:  # r p s
                                rps = rps + 1
                        elif List[len(List) - 2] == 3:  # r s _
                            rs = rs + 1
                            if List[len(List) - 1] == 1:  # r s r
                                rsr = rsr + 1
                            elif List[len(List) - 1] == 2:  # r s p
                                rsp = rsp + 1
                            elif List[len(List) - 1] == 3:  # r s s
                                rss = rss + 1


                    elif List[len(List) - 3] == 2:  # p _ _
                        if List[len(List) - 2] == 1:  # p r _
                            pr = pr + 1
                            if List[len(List) - 1] == 1:  # p r r
                                prr = prr + 1
                            elif List[len(List) - 1] == 2:  # p r p
                                prp = prp + 1
                            elif List[len(List) - 1] == 3:  # p r s
                                prs = prs + 1


                        elif List[len(List) - 2] == 2:
                            pp = pp + 1
                            if List[len(List) - 1] == 1:  # p p r
                                ppr = ppr + 1
                            elif List[len(List) - 1] == 2:  # p p p
                                ppp = ppp + 1
                            elif List[len(List) - 1] == 3:  # p p s
                                pps = pps + 1
                        elif List[len(List) - 2] == 3:
                            ps = ps + 1
                            if List[len(List) - 1] == 1:  # p s r
                                psr = psr + 1
                            elif List[len(List) - 1] == 2:  # p s p
                                psp = psp + 1
                            elif List[len(List) - 1] == 3:  # p s s
                                pss = pss + 1


                    elif List[len(List) - 3] == 3:  # s _ _
                        if List[len(List) - 2] == 1:  # s r _
                            sr = sr + 1
                            if List[len(List) - 1] == 1:  # s r r
                                srr = srr + 1
                            elif List[len(List) - 1] == 2:  # s r p
                                srp = srp + 1
                            elif List[len(List) - 1] == 3:  # s r s
                                srs = srs + 1
                        elif List[len(List) - 2] == 2:  # s p _
                            sp = sp + 1
                            if List[len(List) - 1] == 1:  # s p r
                                spr = spr + 1
                            elif List[len(List) - 1] == 2:  # s p p
                                spp = spp + 1
                            elif List[len(List) - 1] == 3:  # s p s
                                sps = sps + 1
                        elif List[len(List) - 2] == 3:
                            ss = ss + 1
                            if List[len(List) - 1] == 1:  # s s r
                                ssr = ssr + 1
                            elif List[len(List) - 1] == 2:  # s s p
                                ssp = ssp + 1
                            elif List[len(List) - 1] == 3:  # s s s
                                sss = sss + 1

                    # print("##################################################")
                    if rr != 0:
                        mean_val_RR_R = rrr / rr
                        mean_val_RR_P = rrp / rr
                        mean_val_RR_S = rrs / rr

                        triRRR = stats.binom_test(rrr, n=rr, p=0.333, alternative='two-sided')
                        triRRP = stats.binom_test(rrp, n=rr, p=0.333, alternative='two-sided')
                        triRRS = stats.binom_test(rrs, n=rr, p=0.333, alternative='two-sided')

                        # print("binomial test sum for RRR=", triRRR)
                        # print("binomial test sum for RRP=", triRRP)
                        # print("binomial test sum for RRS=", triRRS)

                    # print("##################################################")
                    if rp != 0:
                        mean_val_RP_R = rpr / rp
                        mean_val_RP_P = rpp / rp
                        mean_val_RP_S = rps / rp

                        triRPR = stats.binom_test(rpr, n=rp, p=0.333, alternative='two-sided')
                        triRPP = stats.binom_test(rpp, n=rp, p=0.333, alternative='two-sided')
                        triRPS = stats.binom_test(rps, n=rp, p=0.333, alternative='two-sided')

                        # print("binomial test sum for RPR=", triRPR)
                        # print("binomial test sum for RPP=", triRPP)
                        # print("binomial test sum for RPS=", triRPS)

                    # print("##################################################")
                    if rs != 0:
                        mean_val_RS_R = rsr / rs
                        mean_val_RS_P = rsp / rs
                        mean_val_RS_S = rss / rs

                        triRSR = stats.binom_test(rsr, n=rs, p=0.333, alternative='two-sided')
                        triRSP = stats.binom_test(rsp, n=rs, p=0.333, alternative='two-sided')
                        triRSS = stats.binom_test(rss, n=rs, p=0.333, alternative='two-sided')

                        # print("binomial test sum for RSR=", triRSR)
                        # print("binomial test sum for RSP=", triRSP)
                        # print("binomial test sum for RSS=", triRSS)

                    # print("##################################################")
                    if pr != 0:
                        mean_val_PR_R = prr / pr
                        mean_val_PR_P = prp / pr
                        mean_val_PR_S = prs / pr

                        triPRR = stats.binom_test(prr, n=pr, p=0.333, alternative='two-sided')
                        triPRP = stats.binom_test(prp, n=pr, p=0.333, alternative='two-sided')
                        triPRS = stats.binom_test(prs, n=pr, p=0.333, alternative='two-sided')

                        # print("binomial test sum for PRR=", triPRR)
                        # print("binomial test sum for PRP=", triPRP)
                        # print("binomial test sum for PRS=", triPRS)

                    # print("##################################################")
                    if pp != 0:
                        mean_val_PP_R = ppr / pp
                        mean_val_PP_P = ppp / pp
                        mean_val_PP_S = pps / pp

                        triPPR = stats.binom_test(ppr, n=pp, p=0.333, alternative='two-sided')
                        triPPP = stats.binom_test(ppp, n=pp, p=0.333, alternative='two-sided')
                        triPPS = stats.binom_test(pps, n=pp, p=0.333, alternative='two-sided')

                        # print("binomial test sum for PPR=", triPPR)
                        # print("binomial test sum for PPP=", triPPP)
                        # print("binomial test sum for PPS=", triPPS)

                    # print("##################################################")
                    if ps != 0:
                        mean_val_PS_R = psr / ps
                        mean_val_PS_P = psp / ps
                        mean_val_PS_S = pss / ps

                        triPSR = stats.binom_test(psr, n=ps, p=0.333, alternative='two-sided')
                        triPSP = stats.binom_test(psp, n=ps, p=0.333, alternative='two-sided')
                        triPSS = stats.binom_test(pss, n=ps, p=0.333, alternative='two-sided')

                        # print("binomial test sum for PSR=", triPSR)
                        # print("binomial test sum for PSP=", triPSP)
                        # print("binomial test sum for PSS=", triPSS)

                    # print("##################################################")
                    if sr != 0:
                        mean_val_SR_R = srr / sr
                        mean_val_SR_P = srp / sr
                        mean_val_SR_S = srs / sr

                        triSRR = stats.binom_test(srr, n=sr, p=0.333, alternative='two-sided')
                        triSRP = stats.binom_test(srp, n=sr, p=0.333, alternative='two-sided')
                        triSRS = stats.binom_test(srs, n=sr, p=0.333, alternative='two-sided')

                        # print("binomial test sum for SRR=", triSRR)
                        # print("binomial test sum for SRP=", triSRP)
                        # print("binomial test sum for SRS=", triSRS)

                    # print("##################################################")
                    if sp != 0:
                        mean_val_SP_R = spr / sp
                        mean_val_SP_P = spp / sp
                        mean_val_SP_S = sps / sp

                        triSPR = stats.binom_test(spr, n=sp, p=0.333, alternative='two-sided')
                        triSPP = stats.binom_test(spp, n=sp, p=0.333, alternative='two-sided')
                        triSPS = stats.binom_test(sps, n=sp, p=0.333, alternative='two-sided')

                        # print("binomial test sum for SPR=", triSPR)
                        # print("binomial test sum for SPP=", triSPP)
                        # print("binomial test sum for SPS=", triSPS)

                    # print("##################################################")
                    if ss != 0:
                        mean_val_SS_R = ssr / ss
                        mean_val_SS_P = ssp / ss
                        mean_val_SS_S = sss / ss

                        triSSR = stats.binom_test(ssr, n=ss, p=0.333, alternative='two-sided')
                        triSSP = stats.binom_test(ssp, n=ss, p=0.333, alternative='two-sided')
                        triSSS = stats.binom_test(sss, n=ss, p=0.333, alternative='two-sided')

                        # print("binomial test sum for SSR=", triSSR)
                        # print("binomial test sum for SSP=", triSSP)
                        # print("binomial test sum for SSS=", triSSS)

                    if List[len(List) - 2] == 1 and List[len(List) - 1] == 1:  # r r _ durumu
                        define = max(triRRR, triRRP, triRRS)
                        if define == triRRR:
                            b = 2
                        elif define == triRRP:
                            b = 3
                        elif define == triRRS:
                            b = 1
                    elif List[len(List) - 2] == 1 and List[len(List) - 1] == 2:  # r p _ durumu
                        define = max(triRPR, triRPP, triRPS)
                        if define == triRPR:
                            b = 2
                        elif define == triRPP:
                            b = 3
                        elif define == triRPS:
                            b = 1
                    elif List[len(List) - 2] == 1 and List[len(List) - 1] == 3:  # r s _ durumu
                        define = max(triRSR, triRSP, triRSS)
                        if define == triRSR:
                            b = 2
                        elif define == triRSP:
                            b = 3
                        elif define == triRSS:
                            b = 1
                    elif List[len(List) - 2] == 2 and List[len(List) - 1] == 1:  # p r _ durumu
                        define = max(triPRR, triPRP, triPRS)
                        if define == triPRR:
                            b = 2
                        elif define == triPRP:
                            b = 3
                        elif define == triPRS:
                            b = 1
                    elif List[len(List) - 2] == 2 and List[len(List) - 1] == 2:  # p p _ durumu
                        define = max(triPPR, triPPP, triPPS)
                        if define == triPPR:
                            b = 2
                        elif define == triPPP:
                            b = 3
                        elif define == triPPS:
                            b = 1
                    elif List[len(List) - 2] == 2 and List[len(List) - 1] == 3:  # p s _ durumu
                        define = max(triPSR, triPSP, triPSS)
                        if define == triPSR:
                            b = 2
                        elif define == triPSP:
                            b = 3
                        elif define == triPSS:
                            b = 1

                    elif List[len(List) - 2] == 3 and List[len(List) - 1] == 1:  # s r _ durumu
                        define = max(triSRR, triSRP, triSRS)
                        if define == triSRR:
                            b = 2
                        elif define == triSRP:
                            b = 3
                        elif define == triSRS:
                            b = 1


                    elif List[len(List) - 2] == 3 and List[len(List) - 1] == 2:  # s p _ durumu

                        define = max(triSPR, triSPP, triSPS)
                        if define == triSPR:
                            b = 2
                        elif define == triSPP:
                            b = 3
                        elif define == triSPS:
                            b = 1
                    elif List[len(List) - 2] == 3 and List[len(List) - 1] == 3:  # s s _ durumu

                        define = max(triSSR, triSSP, triSSS)
                        if define == triSSR:
                            b = 2
                        elif define == triSSP:
                            b = 3
                        elif define == triSSS:
                            b = 1

                # print(b)
                sum = a + b
                if b == 1:
                    print("Rock")
                elif b == 2:
                    print("Paper")
                elif b == 3:
                    print("Scissors")

                if b == a:
                    print("draw")
                    a_way = False
                    d_Score += 1
                elif b != a:
                    # print("not raw")
                    if sum == 3:
                        if a == 2:
                            print("You Win")
                            a_way = True
                            c = b
                            w_Score += 1
                        else:
                            print("You Lose")
                            a_way = False

                            l_Score += 1

                    if sum == 4:
                        if a == 1:
                            print("You Win")
                            a_way = True
                            c = b
                            w_Score += 1

                        else:
                            print("You Lose")
                            a_way = False

                            l_Score += 1
                if sum == 5:
                    if a == 3:
                        print("You Win")
                        a_way = True
                        c = b
                        w_Score += 1

                    else:
                        print("You Lose")
                        a_way = False

                        l_Score += 1
            print("your Score=", w_Score)
            print("your tie Score=", d_Score)
            print("Computer Score=", l_Score)
            # print(rr, rs, rp, ss, sp, sr, pr, ps, pp)
            # print(List)
    ###############################################
    elif ant==0:
            game=False
    else:
        print("please choose avaiable number!!")

print("thanks for play with us:)")