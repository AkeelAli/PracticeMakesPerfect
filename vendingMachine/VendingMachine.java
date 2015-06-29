public class VendingMachine {

    public static final int QUARTER_IDX = 0;
    public static final int DIME_IDX = 1;
    public static final int NICKEL_IDX = 2;
    public static final int MAX_IDX = 3;

    public static final int QUARTER = 25;
    public static final int DIME = 10;
    public static final int NICKEL = 5;

    public static final int coinValue[] = {QUARTER, DIME, NICKEL}; 


    /* Member */
    public int coins[]; 

    public VendingMachine(int quarters, int dimes, int nickels) {
        coins = new int[MAX_IDX];

        coins[QUARTER_IDX] = quarters;
        coins[DIME_IDX] = dimes;
        coins[NICKEL_IDX] = nickels;
    
    }

    /**
     * Change is in pennies
     **/
    public void processChange(int change) {
        if (change <= 0) return;

        int coinsReturned[] = new int[MAX_IDX];

        for (int index = QUARTER_IDX;
                index < MAX_IDX; index++) {

            coinsReturned[index] = change / coinValue[index];
            
            if (coinsReturned[index] > 0) {
                int rem_q = coins[index] - coinsReturned[index];
    
                if (rem_q > 0) {
                    coins[index] = rem_q;
                } else {
                    coinsReturned[index] = coins[index];
                    coins[index] = 0;
                }
                   
                change -= coinsReturned[index] * coinValue[index];
            }

        }

        System.out.println(coinsReturned);

    }

    
}
