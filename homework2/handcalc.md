1. P(Cloudy) = <0.5, 0.5> (given by network)
2. P(Sprinkler | Cloudy) = <0.10, 0.50> (given by network)
3. P(Cloudy | Sprinkler ^ ¬Rain)
   = α < P(Cloudy | Sprinkler ^ ¬Rain), P(¬Cloudy | Sprinkler ^ ¬Rain) >
   = α <( P(Sprinkler | Cloudy) x P(¬Rain | Cloudy) x P(Cloudy) ), 
        ( P(Sprinkler | ¬Cloudy) x P(¬Rain | ¬Cloudy) x P(¬Cloudy) )>
   = α <(0.10 x (1 - 0.80) x 0.5), (0.50 x (1 - 0.20) x 0.50)>
   = α <0.01, 0.2> = (approx) 4.76 x <0.01, 0.2>
   = <0.0476, 0.952>
4. P(WetGrass | Cloudy ^ Sprinkler ^ Rain)
   = α < P(WetGrass | Cloudy ^ Sprinkler ^ Rain), P(¬WetGrass | Cloudy ^ Sprinkler ^ Rain) >
   = α < P(Sprinkler | Cloudy) x P(Rain | Cloudy) x P(WetGrass | Sprinkler ^ Rain),
         P(Sprinkler | Cloudy) x P(Rain | Cloudy) x P(¬WetGrass | Sprinkler ^ Rain) >
   = α < (0.10 x 0.80 x 0.99), ( 0.10 x 0.80 x (1 - 0.99) ) >
   = α <0.0792, 0.0008> = 12.5 x <0.0792, 0.0008>
   = <0.99, 0.01>
5. P(Cloudy | ¬WetGrass) = < P(Cloudy | ¬WetGrass), P(¬Cloudy | ¬WetGrass) >
   = α < ( P(C) x P(¬WG | S ^ R) x P(S | C) x P(R | C) )
         + ( P(C) x P(¬WG | ¬S ^ R) x P(¬S | C) x P(R | C) )
         + ( P(C) x P(¬WG | S ^ ¬R) x P(S | C) x P(¬R | C) )
         + ( P(C) x P(¬WG | ¬S ^ ¬R) x P(¬S | C) x P(¬R | C) ),
         ( P(¬C) x P(¬WG | S ^ R) x P(S | ¬C) x P(R | ¬C) )
         + ( P(¬C) x P(¬WG | ¬S ^ R) x P(¬S | ¬C) x P(R | ¬C) )
         + ( P(¬C) x P(¬WG | S ^ ¬R) x P(S | ¬C) x P(¬R | ¬C) )
         + ( P(¬C) x P(¬WG | ¬S ^ ¬R) x P(¬S | ¬C) x P(¬R | ¬C) ) >
   = α < (0.5 x (1 - 0.99) x 0.10 x 0.80)
         + (0.5 x (1 - 0.90) x (1 - 0.10) x 0.80)
         + (0.5 x (1 - 0.90) x 0.10 x (1 - 0.80) )
         + (0.5 x 1 x (1 - 0.10) x (1 - 0.80) ),
         (0.5 x (1 - 0.99) x 0.50 x 0.20)
         + (0.5 x (1 - 0.90) x 0.50 x 0.20)
         + (0.5 x (1 - 0.90) x 0.50 x (1 - 0.20) )
         + (0.5 x 1 x 0.50 x (1 - 0.20) ) >
   = α <0.1274, 0.2255> = (approx) 2.83 x <0.1274, 0.2255>
   = <0.361, 0.639>