public class Main
{
    public static void main(String[] args) {
        HouseTemplate houseType = new WoodenHouse();
        houseType.buildHouse();
        
        System.out.println("--------------------------------------");
        
        houseType = new BrickHouse();
        houseType.buildHouse();
    }
}