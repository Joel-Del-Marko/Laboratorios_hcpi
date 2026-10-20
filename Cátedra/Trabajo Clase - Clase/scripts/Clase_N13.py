#En los dias dde verano: Esrcibe una consulta en panadas 
# en la que encunetres todos los dias donde la generacion 
# solar (Solar) haya superado los 180 GWh y simultaneamente el consumo (Consumption) 
# haya sido moderadoo bajo (menor a 1300 GWh), ¿Cuantos? 

filtro_sobregen = (dt['Solar']>180) & (dt['Consumption']<1300));
dias_sobregen = dt[filtro_sobregen];
print(f"Días de sobregeneración detectados: {len(dias_sobregen)}")
