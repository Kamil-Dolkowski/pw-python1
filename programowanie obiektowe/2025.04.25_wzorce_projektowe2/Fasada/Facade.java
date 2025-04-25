public class Facade {
    public static enum StorageType {
        MYSQL, JSON;
    }
    
    public static enum OutputType {
        REPORT_PDF, DATA_CSV;
    }
    
    public static void generateOutput(StorageType sType, OutputType oType, String resourceName, String outputName) {
        Connection con = null;
        
        if (sType.equals(StorageType.MYSQL)) {
            con = MySQLHelper.getMySQLDBConnection();
            MySQLHelper storage = new MySQLHelper();
            
            if (resourceName.equals("person")) 
                resourceName = "TBL_PERSON";
            else if (resourceName.equals("car"))
                resourceName = "TBL_CAR";
            
            switch (oType) {
                case REPORT_PDF:
                    storage.generateMySQLPDFReport(con, resourceName, outputName);
                    break;
                case DATA_CSV:
                    storage.generateMySQLRawDataCSV(con, resourceName, outputName);
                    break;
            }
        } else if (sType.equals(StorageType.JSON)) {
            con = JSONHelper.getJSONConnection();
            JSONHelper storage = new JSONHelper();
            
            if (resourceName.equals("person")) 
                resourceName = "person.json";
            else if (resourceName.equals("car"))
                resourceName = "car.json";
            
            switch (oType) {
                case REPORT_PDF:
                    storage.generateJSONPDFReport(con, resourceName, outputName);
                    break;
                case DATA_CSV:
                    storage.generateJSONRawDataCSV(con, resourceName, outputName);
                    break;
            }
        }
    }
}