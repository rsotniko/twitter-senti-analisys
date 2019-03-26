package sample;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

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

    }
}
