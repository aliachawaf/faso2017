package fr.sanchez.alexis.smartspeakers;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import fr.sanchez.alexis.smartspeakers.bluetoothconnection.BluetoothClient;


public class MainActivity extends AppCompatActivity {

    BluetoothClient blClient;
    BluetoothAdapter bluetoothAdapter;
    BluetoothDevice enceinte;
    private String recherce_barre;
    //true = en pause false = en marche
    private Boolean etatPlayerPause = true;

    //B8:27:EB:81:08:94 adr mac de bob
    private static final String ADRESSE_MAC_ENCEINTE = "B8:27:EB:81:08:94";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        enceinte = bluetoothAdapter.getRemoteDevice(ADRESSE_MAC_ENCEINTE);
        blClient = new BluetoothClient(enceinte);
        //musique precedente
        final ImageButton btnMusicLeft = (ImageButton) findViewById(R.id.music_left);
        btnMusicLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                envoyerInfoEnceinte("1");
            }
        });
        //musique suivante
        ImageButton btnMusicRight = (ImageButton) findViewById(R.id.music_right);
        btnMusicRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                envoyerInfoEnceinte("0");
            }
        });
        //augmenter volume
        ImageButton btnMusicUp = (ImageButton) findViewById(R.id.vol_up);
        btnMusicUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                envoyerInfoEnceinte("2");
            }
        });
        //baisser volume
        ImageButton btnMusicDown = (ImageButton) findViewById(R.id.vol_down);
        btnMusicDown.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                envoyerInfoEnceinte("3");
            }
        });
        final ImageButton btnMusicPlay = (ImageButton) findViewById(R.id.music_play);
        btnMusicPlay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(etatPlayerPause) {
                    etatPlayerPause=false;
                    btnMusicPlay.setBackground(getResources().getDrawable(R.drawable.pause));
                    //Play
                    envoyerInfoEnceinte("4");
                }else{
                    etatPlayerPause=true;
                    btnMusicPlay.setBackground(getResources().getDrawable(R.drawable.play));
                    //Pause
                    envoyerInfoEnceinte("4");
                }
            }
        });
        Button btn = (Button) findViewById(R.id.button_recherche);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView recherche = (TextView)findViewById(R.id.barre_recherce);
                recherce_barre = recherche.getText().toString();
                etatPlayerPause = false;
                btnMusicPlay.setBackground(getResources().getDrawable(R.drawable.pause));
                envoyerInfoEnceinte("5 " + recherce_barre);
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
