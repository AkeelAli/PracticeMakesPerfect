public class Main {

    public static void main(String args[]) {
        VendingMachine vm = new VendingMachine(2,5,10);

        System.out.println("30:");
        vm.processChange(30);
        
        System.out.println("30:");
        vm.processChange(30);
        
        System.out.println("30:");
        vm.processChange(30);
    }

}
