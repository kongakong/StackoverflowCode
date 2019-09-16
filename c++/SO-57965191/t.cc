   
#include <iostream>
#include <string>
using namespace std;
int x;
int points = 5;
int strength = 5;
int perception = 5;
int endurance = 5;
int charisma = 5;
int intelligence = 5;
int agility = 5;
int luck = 5;
int guns = 15;
int unarmed = 15;
int explosives = 15;
int energyWeapons = 15;
int meleeWeapons = 15;
int repair = 15;
int speech = 15;
int barter = 15;
int sneak = 15;
int lockpick = 15;
int medicine = 15;
int survival = 15;
int science = 15;
int health = 100;
int actionPoints = 100;
int critHitchance = 55;
int skillPoints = 15;
int carryWeight = 120;
class special
{
public:
    void choice()
    {
        do {
            cout << "********************************************************************" << endl;
            cout << "Please choose your SPECIAL stats using Vigor-matic Testing machine." << endl;
            cout << "************************************************************" << endl;
            cout << "You have " << points << " points to distribute." << endl;
            cout << "************************************************************" << endl;
            cout << "How would you like to distribute your points?" << endl;
            cout << "1)Strength" << endl;
            cout << "2)ModifyStrengthValue?" << endl;
            cout << "3)Perception" << endl;
            cout << "4)ModifyPerceptionValue?" << endl;
            cout << "5)Endurance" << endl;
            cout << "6)ModifyEnduranceValue?" << endl;
            cout << "7)Charisma" << endl;
            cout << "8)ModifyCharismaValue?" << endl;
            cout << "9)Intelligence" << endl;
            cout << "10)ModifyIntelligenceValue?" << endl;
            cout << "10)Agility" << endl;
            cout << "11)ModifyAgilityValue?" << endl;
            cout << "12)Luck" << endl;
            cout << "13)ModifyLuckValue?" << endl;
            cout << "14)Would you like to see your current SPECIAL?" << endl;
            cout << "*********************************************************************" << endl;
            cin >> x;
            switch (x)
            {
            case 1:
                    cout << "Strength: " << strength << endl;
                    points--;
                    strength += 1;
                    meleeWeapons += 2;
                    unarmed += 2;
                    carryWeight += 10;
                    cout << "Your Strength points are now: " << strength << endl;
                    cout << "Your Carryweight is now: " << carryWeight << endl;
                    cout << "Your Unarmed combat skill: " << unarmed << endl;
                    cout << "Your Melee Weapons skill is now: " << meleeWeapons << endl;
                    system("PAUSE");
                    break;

            case 2:
                cout << "Strength: " << strength << endl;
                points++;
                strength -= 1;
                meleeWeapons -= 2;
                unarmed -= 2;
                carryWeight -= 10;
                cout << "Your Strength points are now: " << strength << endl;
                cout << "Your Carryweight is now: " << carryWeight << endl;
                cout << "Your Unarmed combat skill: " << unarmed << endl;
                cout << "Your Melee Weapons skill is now: " << meleeWeapons << endl;
                system("PAUSE");
                break;
            case 3:
                    cout << "Perception:" << perception << endl;
                    points--;
                    perception += 1;
                    energyWeapons += 5;
                    cout << "Your Perception points are now: " << perception << endl;
                    cout << "Your EnergyWeapons are now: " << energyWeapons << endl;
                    cout << "Explosives skill is now: " << explosives << endl;
                break;
            case 4:
                cout << "Perception:" << perception << endl;
                points++;
                perception -= 1;
                energyWeapons -= 5;
                explosives -= 5;
                cout << "Your Perception points are now: " << perception << endl;
                cout << "Your EnergyWeapons are now: " << energyWeapons << endl;
                cout << "Explosives skill is now: " << explosives << endl;
                break;
            case 5:
                    cout << "Endurance: " << endurance << endl;
                    points--;
                    endurance += 1;
                    health += 20;
                    cout << "Your Endurance points are now: " << endurance << endl;
                    system("PAUSE");
                break;
            case 6:
                cout << "Endurance: " << endurance << endl;
                points++;
                endurance -= 1;
                health -= 20;
                cout << "Your Endurance points are now: " << endurance << endl;
                system("PAUSE");
                break;
            case 7:
                cout << "Charisma: " << charisma << endl;
                points--;
                charisma += 1;
                speech += 5;
                barter += 5;
                cout << "Your Charisma points are now: " << charisma << endl;
                system("PAUSE");
                break;
            case 8:
                cout << "Charisma: " << charisma << endl;
                points++;
                charisma -= 1;
                speech -= 5;
                barter -= 5;
                cout << "Your Charisma points are now: " << charisma << endl;
                system("PAUSE");
                break;
            case 9:
                cout << "Intelligence: " << intelligence << endl;
                points--;
                intelligence += 1;
                repair += 3;
                science += 3;
                skillPoints += 2;
                cout << "Your Intelligence points are now: " << intelligence << endl;
                cout << "Your repair points are now: " << repair << endl;
                cout << "Your science point are now: " << science << endl;
                system("Pause");
                break;
            case 10:
                cout << "Intelligence: " << intelligence << endl;
                points++;
                intelligence -= 1;
                repair -= 3;
                science -= 3;
                skillPoints -= 2;
                cout << "Your Intelligence points are now: " << intelligence << endl;
                cout << "Your repair points are now: " << repair << endl;
                cout << "Your science point are now: " << science << endl;
                system("Pause");
                break;
            case 11:
                cout << "Agility: " << agility << endl;
                points--;
                agility += 1;
                lockpick += 2;
                actionPoints += 2;
                cout << "Your Agility points are now: " << agility << endl;
                cout << "Your Lockpick points are now: " << lockpick << endl;
                cout << "Your Action Points are now: " << actionPoints << endl;
                system("Pause");
                break;
            case 12:
                cout << "Agility: " << agility << endl;
                points++;
                agility -= 1;
                lockpick -= 2;
                actionPoints -= 2;
                cout << "Your Agility points are now: " << agility << endl;
                cout << "Your Lockpick points are now: " << lockpick << endl;
                cout << "Your Action Points are now: " << actionPoints << endl;
                system("Pause");
                break;

            case 13:
                cout << "Luck:" << luck << endl;
                points--;
                luck += 1;
                critHitchance += 5;
                system("Pause");
                break;
            case 14:
                cout << "Strength: " << strength << endl;
                cout << "Perception: " << perception << endl;
                cout << "Endurance: " << endurance << endl;
                cout << "Charisma: " << charisma << endl;
                cout << "Intelligence: " << intelligence << endl;
                cout << "Agility: " << agility << endl;
                cout << "Luck: " << luck << endl;
                break;
            default:
                cout << "Only Numbers..." << endl;
            }
        } while (points != 0);
    }
};
class skills {

public:
    int n;
    void skillChoice()
    {
        do {
            cout << "****************************************" << endl;
            cout << "Welcome to the Skill distribution system." << endl;
            cout << "You have " << skillPoints << " skill points to distribute." << endl;
            cout << "1)Guns" << endl;
            cout << "2)Explosives" << endl;
            cout << "3)EnergyWeapons" << endl;
            cout << "4)MeleeWeapons" << endl;
            cout << "5)Repair" << endl;
            cout << "6)Speech" << endl;
            cout << "7)Barter" << endl;
            cout << "8)Sneak" << endl;
            cout << "9)Lockpick" << endl;
            cout << "10)Medicine" << endl;
            cout << "11)Survival" << endl;
            cout << "12)Science" << endl;
            cout << "13)Would you like to see your total skill stats?" << endl;
            cin >> n;

            switch (n) {
            case 1:

                skillPoints--;
                guns += 1;

                break;
            case 2:
                skillPoints--;
                explosives += 1;
                break;
            case 3:
                skillPoints--;
                energyWeapons += 1;
                break;
            case 4:
                skillPoints--;
                meleeWeapons += 1;
                break;
            case 5:
                skillPoints--;
                repair += 1;
                break;
            case 6:
                skillPoints--;
                speech += 1;
                break;
            case 7:
                skillPoints--;
                barter += 1;
                break;
            case 8:
                skillPoints--;
                sneak += 1;
                break;
            case 9:
                skillPoints--;
                lockpick += 1;
                break;
            case 10:
                skillPoints--;
                medicine += 1;
                break;
            case 11:
                skillPoints--;
                survival += 1;
                break;
            case 12:
                skillPoints--;
                science += 1;
                break;
            case 13:
                cout << "Your characters hp is " << health << endl;
                cout << "Your characters action points are " << actionPoints << endl;
                cout << "Your carry weight is " << carryWeight << endl;
                cout << "Your critical chance is " << critHitchance << endl;
                cout << "You have " << guns << "points in the Guns Skill." << endl;
                cout << "You have " << explosives << "points in the Explosives Skill." << endl;
                cout << "You have " << energyWeapons << "points in the EnergyWeapons Skill." << endl;
                cout << "You have " << meleeWeapons << "points in the Melee Weapons Skill." << endl;
                cout << "You have " << repair << "points in the Repair Skill." << endl;
                cout << "You have " << speech << "points in the Speech Skill." << endl;
                cout << "You have " << barter << "points in the Barter Skill." << endl;
                cout << "You have " << lockpick << "points in the Lockpick Skill." << endl;
                cout << "You have " << medicine << "points in the Medicine." << endl;
                cout << "You have " << survival << "points in the Survival Skill." << endl;
                cout << "You have " << science << "points in the Science Skill." << endl;
                break;

            default:
                cout << "Please Input Numbers..." << endl;
            }
        } while (skillPoints != 15);

    }
};
int main()
{
    special special;
    skills skill;
    special.choice();
    skill.skillChoice();
    return 0;
}
