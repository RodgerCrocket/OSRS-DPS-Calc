import random
AttackLv    =   int(input("What is your attacking style's base level?: "))
PotionLevel =   int(input("What is your current potion bonus?: "))
PrayerBonus =   int(input("What is your current prayer % bonus?: "))
StyleBonus  =   int(input("What is your style bonus? : "))
ExtraBonus  =   int(input("Any other extra bonuses in %? (Void, etc) : "))



EffectiveA = int( ( (   (AttackLv + PotionLevel) * (1 + PrayerBonus/100) * (1 + ExtraBonus/100) + 8 + StyleBonus) ) )
EquipStats = int(input("What are your equipment stat bonus?: "))

FinalAccuracy = (EffectiveA * (EquipStats + 64))
print ("Overall Accuracy = " +str(FinalAccuracy))

DefenceLv       = int(input("\nWhat is your enemy's base defence?: "            ))
DefPotLevel     = int(input("What is your enemy's current potion bonus?: "      ))
DefPrayBonus    = int(input("What if your enemy's current prayer % bonus?: "    ))
DefStyleBonus   = int(input("What is your enemy's style bonus?: "               ))
DefExtraBonus   = int(input("What are your enemy's extra bonuses in %?: "       ))

EffectiveD = int( ( (   (DefenceLv + DefPotLevel) * (1 + DefPrayBonus/100) * (1 + DefExtraBonus/100) + 8 + DefStyleBonus) ) )
DefStats = int(input("What is your enemy's equipment stat bonus?: "))

FinalDefence = (EffectiveD * (64 + DefStats))
print ("Overall Defence = " +str(FinalDefence))

if FinalAccuracy < FinalDefence:
    Result = ( ( FinalAccuracy - 1) / (2 * FinalDefence) )
    
elif FinalAccuracy > FinalDefence:
    Result = ( 1 - ( FinalDefence + 1) / (2 * FinalAccuracy) )

else:
    Result = 0.5

StrengthLv = int(input("\nWhat is your current Strength/Ranged level?: "))
StrPotLevel = int(input("What is your current potion bonus to said level?: "))
StrPrayBonus =   int(input("What is your current prayer % bonus?: "))
StrStyleBonus  =   int(input("What is your style bonus? : "))
StrExtraBonus  =   int(input("Any other extra bonuses in %? (Void, etc) : "))

EffectiveS = int( ( (   (StrengthLv + StrPotLevel) * (1 + StrPrayBonus/100) * (1 + StrExtraBonus/100) + StrStyleBonus) ) )


StrStats = int(input("What is your Strength/Ranged Strength stat bonus?: "))
BaseDamage = 1.3 + (EffectiveS/10) + (StrStats/80) + ((EffectiveS * StrStats)/640)
SpecialBonus = int(input("Any extra multipliers (check wiki): "))

FinalDamage = int(BaseDamage * (1 + SpecialBonus/100))

WepSpeed = int(input("\nWhat is your weapon speed in ticks? One tick = 0.6s | Whip is 4, so on, just wiki it: "))
AttacksPerHour = int(6000/WepSpeed)

PlayTime = (int(input("\nHow many seconds will you play for? - ")))
numAttacksTotal = int(PlayTime/WepSpeed)

XPEarned = 0
for x in range (0, numAttacksTotal):
    RNG = random.randint(0,100)
    if RNG > (100 - (Result * 100)):
        Damage = random.randint(0,FinalDamage)
        XPEarned += (4 * Damage)
        
for y in range (0,50):
    print ("")
    
print ("Max Hit = " +str(FinalDamage))
print ("You have a " +str(round(Result * 100, 4)) +"% chance of hitting your enemy.")
print ("Simulation Ran, AVG XP/hr assuming perfect: " +str(XPEarned))
print ("AVG XP imperfect: " +str(XPEarned * 0.9))
