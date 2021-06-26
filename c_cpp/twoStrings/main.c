#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/*
 *
 * return "YES" if strings have a char in common
 *
 */
char* twoStrings(char* s1, char* s2) {
    int s1_count[256] = {0}; 
    int s2_count[256] = {0};
    int i = 0;
    char c;
    char b;
    for (i = 0; i < strlen(s1); ++i) {
	c = s1[i];
	printf("processing %c\n", c);
        s1_count[c] = 1;
	printf("   count %d\n", s1_count[c]);
    }
    for (i = 0; i < strlen(s2); ++i) {
	c = s2[i];
	printf("processing %c\n", c);
        s2_count[c] = 1;
	printf("   count %d\n", s2_count[c]);
    }
    for (i = 'a'; i <= 'z'; ++i) {
	printf("%c is found %d in s1 and %d in s2\n", i, s1_count[i], s2_count[i]);
        if (s1_count[i] > 0 && s2_count[i] > 0) {
            return "YES";
        }
    }
    return "NO";
}

int main(void) {
  printf("%s\n", twoStrings("akhmlhkvkgifrzteluvtxozdzubndlofrmkfbhykpoftuxanpbpjtirjafczsgdwabyiglxxqoybgyjzeysysfsrqwtsdboahbedvxfgsecnwedpnavdplzgrhlljtazfmvsskfdizvqsyttcgjsmegevzhcjvjajhejyjjmgmxbvowcethwfetdtcnrehwvxswhhaunmxfevefwmxkdfduvwhouihwbybjbzvftlkxyqcwnzsvhtubfngdgqqckemchqmjzvqaxslfslhqpakrvvdlkcmstmkgixpzdcqzrhmbvqemrvumskelnjewrotbxoblsgrwwfjhgjgdsmgougrilnypahdzbcxlqjipxjsbodijlupmwfqbvexliinvvtqnkbnntyzuehiednnmipcjshdqlvfoggvqwjwrevsahailkvwumyxmaaluceuxebsmajghuazflafyfkvslrvixthqzjjpbtkzygxendcrcxiqzlntxdxwkkjggkvnvkonbtwxzillgooeglptbdgnerxnebufesbooaamtovtnqtakytiasbrwztadidctxebyxijuwdcesjmcloexorzubpcniakujoymddhxydciliuesdymhiapjflaqnezbjxxlkwdklxmkwupewetsomwcxjhnaiyivlwuqcvcasgfdjmeziyyxzpjfpyiaqxjhmcdaodfzvzasvmffnqdzwygmiexdynpygariejxfbbtzqoivfvvhxqflwrshyxyyjzdosnnhkcoxxiyqmmxrfspzfouvhktrirnhubhrkwhkgwozhcswlgutidyanbjwnbykrrrmnbqkksdrosihupxicpmdtudocqxmbqziwrggyoucqqboykzwsmcgfvncckomscrpjeskcnakitikjwxhonunxbiqlwlexfjuphkyizrocqpvrajpnx", "bdsyakcbmwqxpxezqjvhgtmeiosnzkvdfcqvhsbxbwjkliqgjqghnhhuqipoujyervbiedrrijvyqdldgahihygfvrgrznfwarenoopadpcyklrdgvaxumgaqftbxzhqmjoyansyrisizsrbmemzcexbyvfphgyuevbtxzhfelrvnsjggjguikgihaktstlwnjalswntgtbuwxeobbamqnpeuyzlqekodxpwfncpvvjlruedimkeyrzulzlujzslpgzckcewptdbsymwxajwoduyadioedqrivynyluxrrnxgnxrhaawrmjdjstshvoalbbcsnljokjxddshemgzxvdwhtirvqfqatmrriitbsqqbuaijcadxxwvhljgdbhwoeyubidwyotntqqniipxxqwhhdiklxalgdxbakhcspvvajeksvdnwboofuqswfgwyfphkidkaesyqxwoaenmfkrtjuhbsqeubrnwhrkkcmnsrkdxasqbggeelihesfttztfdrqprmwnihvbjcppphfmjvoarsxvsfrsontpyvzgmrvesugdkqcxvrjyrrxdmpeadscxtuptherqkyytlufepjfkmkswbrlosyzouisliwddsvkxtisgsqxgadybzintzndjorccyrcgfpajwuutprhplzwpizzkggbgmnxxtrjrxnxldjfmbenhdzjjarpzaisehejgxejxdzvesafkvtvhgphafwtoiekvlawepmgjofyqjxzkzsdyeyqfenplhhsaxdpewpcclphglfrxunxuaycujzteyqcypohvyxlbuaugfcgiwmpimsqxayivaazxaoisoukipqpxkcivicevsorfoajbntsfhiologjjwwolwwbpvexuwipqomgclpfjxlcq"));
  return 0;
}
