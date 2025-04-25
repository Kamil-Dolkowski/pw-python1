public class JSONHelper {
    public static Connection getJSONConnection() {
        return new Connection("JSON File(s)");
    }
    
    public void generateJSONPDFReport(Connection con, String file, String outFileName) {
        System.out.println("Get data from JSON file '" + file + "', generate report in PDF format and save as '" + outFileName + "'");
    }
    
    public void generateJSONRawDataCSV(Connection con, String file, String outFileName) {
        System.out.println("Get raw data from JSON file '" + file + "' in CSV format and save as '" + outFileName + "'");
    }
}