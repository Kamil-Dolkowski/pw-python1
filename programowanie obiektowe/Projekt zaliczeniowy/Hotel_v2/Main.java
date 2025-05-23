import java.util.ArrayList;
import java.util.List;

public class Main 
{
    public static void main(String[] args) {
        System.out.println("##### ========== PRACOWNIK ========== #####\n");

        CommandExecutor employee = new CommandProxy("employee", "hotel123");

        employee.addRoom(RoomFactory.getRoom("standard", "5", 12.0, 2, 60.0));
        employee.addRoom(RoomFactory.getRoom("luxury", "6", 20.0, 1, 200.0));
        employee.addRoom(RoomFactory.getRoom("cheap", "7A", 10.0, 2, 40.0));

        employee.showAllAvailableRooms();
        employee.reserveRoom("5");
        employee.removeRoom("6");
        employee.showAllAvailableRooms();
        employee.cancelReservation("5");


        System.out.println("\n##### ========== KLIENT ========== #####\n");

        CommandExecutor client = new CommandProxy("client", "client123");

        client.addRoom(RoomFactory.getRoom("standard", "5", 12.0, 2, 60.0));
        client.reserveRoom("6");
        client.showAllAvailableRooms();
    }
}