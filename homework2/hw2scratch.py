from probability import BayesNet, enumeration_ask

T, F = True, False

weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {
     (T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
])

print('P(Cloudy):')
print('\t' + enumeration_ask('Cloudy', dict(), weather).show_approx())

print('P(Cloudy | Sprinkler):')
print('\t' + enumeration_ask('Sprinkler', dict(Cloudy=T), weather).show_approx())

print('P(Cloudy | Sprinkler ^ ¬Rain):')
print('\t' + enumeration_ask('Cloudy',
                             dict(Sprinkler=T, Rain=F), weather).show_approx())

print('P(WetGrass | Cloudy ^ Sprinkler ^ Rain):')
print('\t' + enumeration_ask('WetGrass',
                             dict(Cloudy=T, Sprinkler=T, Rain=T),
                             weather).show_approx())

print('P(Cloudy | ¬WetGrass):')
print('\t' + enumeration_ask('Cloudy', dict(WetGrass=F), weather).show_approx())
