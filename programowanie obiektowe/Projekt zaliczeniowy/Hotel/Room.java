public class Room {
    // Must-have (required) parameters
    private String number;
    private Double area; // m^2
    private int occupancy;
    private Double cost;

    // Optional parameters
    private boolean hasTv;
    private boolean hasFridge;
    private boolean hasBathroom;
    private boolean hasBalcony;
    
    public void info() {
        System.out.println("========== POKÓJ ==========");
        System.out.println(String.format("- Numer: %s", number));
        System.out.println(String.format("- Powierzchnia: %.2f m^2", area));
        System.out.println(String.format("- Rodzaj: %d-osobowy", occupancy));
        System.out.println(String.format("- Koszt: %.2f zł/dobę", cost));

        if (hasTv == true) {
            System.out.println("- Telewizor: Tak");
        } else {
            System.out.println("- Telewizor: Nie");
        }

        if (hasFridge == true) {
            System.out.println("- Lodówka: Tak");
        } else {
            System.out.println("- Lodówka: Nie");
        }

        if (hasBathroom == true) {
            System.out.println("- Łazienka: Tak");
        } else {
            System.out.println("- Łazienka: Nie");
        }

        if (hasBalcony == true) {
            System.out.println("- Balkon: Tak");
        } else {
            System.out.println("- Balkon: Nie");
        }
    }

    private Room(RoomBuilder builder) {
        this.number = builder.number;
        this.area = builder.area;
        this.occupancy = builder.occupancy;
        this.cost = builder.cost;

        this.hasTv = builder.hasTv;
        this.hasFridge = builder.hasFridge;
        this.hasBathroom = builder.hasBathroom;
        this.hasBalcony = builder.hasBalcony;
    }

    public static class RoomBuilder {
        // Must-have (required) parameters
        private String number;
        private Double area; // m^2
        private int occupancy;
        private Double cost;

        // Optional parameters
        private boolean hasTv;
        private boolean hasFridge;
        private boolean hasBathroom;
        private boolean hasBalcony;

        public RoomBuilder(String number, Double area, int occupancy, Double cost) {
            // Must-have (required) parameters
            this.number = number;
            this.area = area;
            this.occupancy = occupancy;
            this.cost = cost;

            // Optional parameters
            this.hasTv = false;
            this.hasFridge = false;
            this.hasBathroom = true;
            this.hasBalcony = false;
        }

        public RoomBuilder hasTv(boolean has) {
            hasTv = has;
            return this;
        }

        public RoomBuilder hasFridge(boolean has) {
            hasFridge = has;
            return this;
        }

        public RoomBuilder hasBathroom(boolean has) {
            hasBathroom = has;
            return this;
        }

        public RoomBuilder hasBalcony(boolean has) {
            hasBalcony = has;
            return this;
        }

        public Room build() {
            return new Room(this);
        }
    }
}