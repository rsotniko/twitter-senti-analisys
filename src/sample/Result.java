package sample;

import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Result extends Application {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button save_button;

    @FXML
    private TextArea resTxt;

    @FXML
    void initialize() {

        if (resTxt == null)
            throw new AssertionError("fx:id=\"resTxt\" was not injected: check your FXML file 'result.fxml'.");

        if (save_button == null)
            throw new AssertionError("fx:id=\"save_button\" was not injected: check your FXML file 'result.fxml'.");

        String _res = "";
        resTxt.setEditable(false);

        try {
            String copy = "";
            int tcounter = 0, fcounter = 0;
            //todo Путь надо изменить
            File file = new File("result.txt");
            //создаем объект FileReader для объекта File
            FileReader fr = new FileReader(file);
            //создаем BufferedReader с существующего FileReader для построчного считывания
            BufferedReader reader = new BufferedReader(fr);
            // считаем сначала первую строку
            String line = reader.readLine();
            while (line != null) {
                _res = _res + line + "\n";
                line = reader.readLine();
            }
            _res = _res.replaceAll("true;", "true\n");
            _res = _res.replaceAll("false;", "false\n");
            _res = _res.replaceAll(";", "\nAnalyze result: ");
            copy = _res;
            _res+= "==========================";
            while (copy.contains("true")||copy.contains("false")) {
                if (_res.contains("true")) {
                    copy = copy.replaceFirst("true", "");
                    tcounter++;
                }
                if (_res.contains("false")) {
                    copy = copy.replaceFirst("false", "");
                    fcounter++;
                }
            }
            _res += "\n\nResult:\ntrue: " + tcounter + "\nfalse: " + fcounter;
            resTxt.setText(_res);
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String final_res = _res;
        save_button.setOnAction(event -> {
            try {
                File file = new File("output.txt");
                file.createNewFile();
                file.setWritable(true);
                FileWriter writer = new FileWriter(file);
                writer.write(final_res);
                System.out.println("Файл output.txt был создан в корневой директории проекта");
                writer.flush();
                writer.close();
            }
            catch (Exception e)
            {
                System.out.println("Не удалось создать файл");
            }
        });

    }





    @Override
    public void start(Stage primaryStage) throws Exception {

    }
}
