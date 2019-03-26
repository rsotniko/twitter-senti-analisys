package sample;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
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
                FXMLLoader fxmlLoader = new FXMLLoader();
                fxmlLoader.setLocation(getClass().getResource("result.fxml"));
                /*
                 * if "fx:controller" is not set in fxml
                 * fxmlLoader.setController(NewWindowController);
                 */
                Scene scene = new Scene(fxmlLoader.load(), 600, 400);
                Stage stage = new Stage();
                stage.setTitle("New Window");
                stage.setScene(scene);
                stage.show();
            } catch (IOException e) {
                Logger logger = Logger.getLogger(getClass().getName());
                logger.log(Level.SEVERE, "Failed to create new Window.", e);
            }
        });
    }
}
