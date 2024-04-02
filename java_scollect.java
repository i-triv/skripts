import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FilterStringInFile {
    public static void main(String[] args) {
        String inputFile = "input.txt";
        String outputFile = "result.txt";
        String filterString = "tmp";

        try {
            // Read the input file content
            BufferedReader reader = new BufferedReader(new FileReader(new File(inputFile)));
            String line;
            StringBuilder filteredContent = new StringBuilder();

            // Filter the content based on the string
            while ((line = reader.readLine()) != null) {
                if (!line.contains(filterString)) {
                    filteredContent.append(line).append("\n");
                }
            }
            reader.close();

            // Write the filtered content to the output file
            FileWriter writer = new FileWriter(new File(outputFile));
            writer.write(filteredContent.toString());
            writer.close();

        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
