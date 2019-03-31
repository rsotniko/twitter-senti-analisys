package sample;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Controller {


    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private TextField num_txt;

    @FXML
    private TextField hashtag_txt;

    @FXML
    private Button run_button;

    @FXML
    void initialize() {
        assert num_txt != null : "fx:id=\"num_txt\" was not injected: check your FXML file 'sample.fxml'.";
        assert hashtag_txt != null : "fx:id=\"hashtag_txt\" was not injected: check your FXML file 'sample.fxml'.";
        assert run_button != null : "fx:id=\"run_button\" was not injected: check your FXML file 'sample.fxml'.";

        run_button.setOnAction(event -> {

            try {
                String hastag = hashtag_txt.getText(); //Поле с хегтегом
                int num = Integer.parseInt(num_txt.getText()); //Поле с кол-вом сообщений

                // Загрузка дополнительного окна, для вывода результата
                FXMLLoader fxmlLoader = new FXMLLoader();
                fxmlLoader.setLocation(getClass().getResource("result.fxml"));
                Scene scene = new Scene(fxmlLoader.load(), 600, 400);
                Stage stage = new Stage();
                stage.setTitle("Result");
                stage.resizableProperty().setValue(false);
                stage.setScene(scene);



                stage.show();

            } catch (Exception e) {

                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error");
                alert.setHeaderText("Invalid input");
                alert.setContentText("Check your input and try again");

                alert.showAndWait();

            }
        });
    }

    @FXML
    void Run(String hashtag, int num) {
        //todo Заупск анализа программы
    }

}

