Ciao, qui si fa fluidodinamica colorata (Male).

Ad ora sappiamo che:
- Sembra molto più consigliabile imporre la temperatura sul profilo e non il flusso di calore
- Dobbiamo trovare dei quantificatori per capire che quantità ci interessano e dobbiamo usare per capire quale sia il nostro obbiettivo finale
- Avere e trovare un obbiettivo finale

// Creato da Matteo il 2024-10-29.

GRANDEZZE UTILIZZATE:
- gas constant (R):         287.058 J/kg*K
- gamma:                    1.4
- pressione asintotica:     101325 Pa       ---> condizione in __outlet__
- temperatura asintotica:   30 °C (303.15 K) 
- densità: rho = p / (R*T)  1.16426 kg/m^3
- velocità asintotica:      7 m/s
- pressione tot:            101353.5 Pa     ---> condizione in __inlet__
- temperatura tot:          303.174 K       ---> condizione in __inlet__
- viscosità dinamica:       1.86078e-5 Pa*s (Sutherland)
- temperatura alette:       80 °C (353.15 K)
- numero di Mach:           0.020054
- lunghezza car. Re:        14e-3 m (altezza condotto)
- numero di Reynolds:       6.13167e+3
- lunghezza car. coeff.:    5.5e-3 m (corda alette)

Per il calcolo, usare __reference_values.m__

// Pietro 12/11/2024

GOOD PRACTICE for linear solver setup:
[click here](https://su2code.github.io/docs_v7/Linear-Solvers-and-Preconditioners/) --> 'Fluid Simulations' section

LINK UTILI
1. STUDIO FLUSSI DA FISICA TECNICA
- http://pcfarina.eng.unipr.it/DispenseTFD/Lezione_Amendola.pdf
- https://www.univpm.it/Entra/Engine/RAServeFile.php/f/P001087/allegati_doc/convezione.pdf
- http://www2.ing.unipi.it/~a080082/Trasmissione%20del%20calore.pdf

2. DOCUMENTAZIONE SU2
- https://su2code.github.io/docs_v7/Physical-Definition/
- https://su2code.github.io/docs_v7/Theory/

// Ilaria 15/11/2024

