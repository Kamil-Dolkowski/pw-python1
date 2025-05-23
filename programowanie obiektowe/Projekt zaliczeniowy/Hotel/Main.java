public class Main 
{
    public static void main(String[] args) {
        Room standardRoom = RoomFactory.getRoom("standard", "5", 12.0, 2, 60.0);
        standardRoom.info();

        Room luxuryRoom = RoomFactory.getRoom("luxury", "6", 20.0, 1, 200.0);
        luxuryRoom.info();

        Room cheapRoom = RoomFactory.getRoom("cheap", "7A", 10.0, 2, 40.0);
        cheapRoom.info();
    }
}