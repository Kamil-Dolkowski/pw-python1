public class RoomFactory {
    public static Room getRoom(String type, String number, Double area, int occupancy, Double cost) {
        if (type.equals("standard")) {
            return new Room.RoomBuilder(number, area, occupancy, cost).build();

        } else if (type.equals("luxury")) {
            return new Room.RoomBuilder(number, area, occupancy, cost).hasTv(true).hasFridge(true).hasBathroom(true).hasBalcony(true).build();

        } else if (type.equals("cheap")) {
            return new Room.RoomBuilder(number, area, occupancy, cost).hasBathroom(false).build();
            
        } else {
            return null;
        }
    }
}