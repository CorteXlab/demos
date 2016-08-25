(ssh airlock) 
ssh -X -v -i .ssh/ -p 2269 trisset@gw.cortexlab.fr
oarsub  -l nodes=BEST,walltime=1:00:00 "sleep 1000000"

/* oarsub  -l nodes=BEST,walltime=48:00:00 -r "2016-03-23 00:00:00"

-> job 204 */

configuration du fftweb (F11 pour plein écran): 
fenetre 1500*150 sur port 6664, décocher rearrange halves
rien sur x, y etre 0 et 3 et title C_IA/C_ref

6 autre graphe 750*150 
1) 6663 UE1 main channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 

2) 6665 UE1 Interfering Channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 

3) 6666 UE2 main channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 

4) 6667 UE2 Interfering Channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 

5) 6668 UE3 main channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 

6) 6669 UE3 Interfering Channel
-32 < x < 32 0 < y < 0.003 
+ Mean window 4 




mimbert
