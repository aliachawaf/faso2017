package fr.sanchez.alexis.smartspeakers;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import fr.sanchez.alexis.smartspeakers.bluetoothconnection.BluetoothClient;


public class MainActivity extends AppCompatActivity {

    BluetoothClient blClient;
    BluetoothAdapter bluetoothAdapter;
    BluetoothDevice enceinte;
    private String recherce_barre;

    //b8:27:e6:26:a2:3e
    private static final String ADRESSE_MAC_ENCEINTE = "B8:27:EB:81:08:94";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        enceinte = bluetoothAdapter.getRemoteDevice(ADRESSE_MAC_ENCEINTE);
        blClient = new BluetoothClient(enceinte);
        Button btn = (Button) findViewById(R.id.button_recherche);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView recherche = (TextView)findViewById(R.id.barre_recherce);
                recherce_barre = recherche.getText().toString();
                envoyerInfoEnceinte(recherce_barre);
            }
        });
    }

    private void envoyerInfoEnceinte(String recherche){
        blClient.write(recherche);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        blClient.cancel();
    }
}
