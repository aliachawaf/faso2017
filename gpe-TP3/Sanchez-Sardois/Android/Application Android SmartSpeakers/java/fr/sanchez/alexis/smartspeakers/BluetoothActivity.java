package fr.sanchez.alexis.smartspeakers;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import java.util.ArrayList;

public class BluetoothActivity extends AppCompatActivity{

    private final static int REQUEST_CODE_ENABLE_BLUETOOTH = 0;
    private BluetoothAdapter bluetoothAdapter;
    private static final String ADRESSE_MAC_ENCEINTE = "B8:27:EB:81:08:94";
    private ArrayList<String> periph = new ArrayList();

    //Fonction appelée à la création de l'activité
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bluetooth);
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if(!(bluetoothAdapter == null)){
            //Requete d'écoute sur les changements d'état du composant Bluetooth
            IntentFilter filter = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
            registerReceiver(bluetoothEcoute, filter);
            IntentFilter filter2 = new IntentFilter(BluetoothDevice.ACTION_FOUND);
            registerReceiver(appareilCo, filter2);
            IntentFilter filter3 = new IntentFilter(BluetoothDevice.ACTION_NAME_CHANGED);
            registerReceiver(appareilCo, filter3);

            if(!bluetoothAdapter.isEnabled()){
                desactiverBluetooth();
            }else{
                activerBluetooth();
            }
            if (isConnectedToBob()){
                Intent intent = new Intent(this, MainActivity.class);
                startActivity(intent);
            }
        }else {
            TextView text = (TextView) findViewById(R.id.bl_no);
            text.setVisibility(View.VISIBLE);
        }
    }

    // Requête d'activation du bluetooth lors de l'appuie sur le bouton
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_CODE_ENABLE_BLUETOOTH)
            return;
        if (resultCode == RESULT_OK) {
            Log.i("SmartSpeakers", "Le bluetooth a été activé");
            activerBluetooth();
        } else {
            Log.e("SmartSpeakers", "Le bluetooth n'a pas été activé");
        }
    }

    // On met a jour l'affichage et l'évent du bouton
    protected void activerBluetooth() {
        TextView text = (TextView) findViewById(R.id.bl_etat);
        text.setText("oui");
        text.setTextColor(Color.GREEN);
        Button btn = (Button) findViewById(R.id.bl_btn);
        btn.setText("Désactiver le bluetooth");

        //cancel any prior BT device discovery
        if (bluetoothAdapter.isDiscovering()){
            bluetoothAdapter.cancelDiscovery();
        }
        bluetoothAdapter.startDiscovery();

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                desactiverBluetooth();
            }
        });
    }

    // On met a jour l'affichage et l'évent du bouton
    protected void desactiverBluetooth(){
        bluetoothAdapter.disable();

        //On met a jour les différents affichages
        TextView text = (TextView)findViewById(R.id.bl_etat);
        text.setText("non");
        text.setTextColor(Color.RED);
        TextView text2 = (TextView)findViewById(R.id.enceinte_etat);
        text2.setText("non");
        text2.setTextColor(Color.RED);
        TextView textView = (TextView)findViewById(R.id.liste_appareils);
        textView.setText("Aucun");

        periph.clear();

        //On met a jour l'action du bouton
        Button btn = (Button)findViewById(R.id.bl_btn);
        btn.setText("Activer le bluetooth");
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent enableBlueTooth = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBlueTooth, REQUEST_CODE_ENABLE_BLUETOOTH);
            }
        });
    }

    // Gestion de l'écoute du bluetooth (activation/desactvation)
    private final BroadcastReceiver bluetoothEcoute = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if (action.equals(BluetoothAdapter.ACTION_STATE_CHANGED)) {
                final int state = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, BluetoothAdapter.ERROR);
                switch (state) {
                    case BluetoothAdapter.STATE_OFF:
                        Toast.makeText(getApplicationContext(), "Bluetooth désactivé", Toast.LENGTH_SHORT).show();
                        desactiverBluetooth();// On met a jour l'affichage et l'évent du bouton
                        break;
                    case BluetoothAdapter.STATE_TURNING_OFF:
                        Toast.makeText(getApplicationContext(), "Désactivation du Bluetooth...", Toast.LENGTH_SHORT).show();
                        break;
                    case BluetoothAdapter.STATE_ON:
                        Toast.makeText(getApplicationContext(), "Bluetooth activé", Toast.LENGTH_SHORT).show();
                        activerBluetooth();// On met a jour l'affichage et l'évent du bouton
                        break;
                    case BluetoothAdapter.STATE_TURNING_ON:
                        Toast.makeText(getApplicationContext(), "Activation du Bluetooth...", Toast.LENGTH_SHORT).show();
                        break;
                }
            }
            bluetoothAdapter.cancelDiscovery();
            bluetoothAdapter.startDiscovery();
        }
    };

    public final BroadcastReceiver appareilCo = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if (action.equals(BluetoothDevice.ACTION_FOUND) || action.equals(BluetoothDevice.ACTION_NAME_CHANGED)) {
                BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                if (!periph.contains(device.getName()))  {
                    periph.add(device.getName());
                    Log.e("Smart Speakers", "Trouvé new appareil");
                    TextView textView = (TextView)findViewById(R.id.liste_appareils);
                    if(textView.getText() == "Aucun"){
                        textView.setText(device.getName());
                    }else if (!textView.getText().toString().contains(device.getName())){
                        textView.setText(textView.getText() + "\n" + device.getName());
                    }
                }
                if(device.getAddress() == ADRESSE_MAC_ENCEINTE){
                    Intent intent2 = new Intent(getApplicationContext(),MainActivity.class);
                    startActivity(intent2);
                }
            }
        }
    };

    @Override
    protected void onDestroy() {
        super.onDestroy();
        bluetoothAdapter.cancelDiscovery();
        unregisterReceiver(appareilCo);
    }

    private boolean isConnectedToBob() {
        if(bluetoothAdapter != null) {
            BluetoothDevice enceinte = bluetoothAdapter.getRemoteDevice(ADRESSE_MAC_ENCEINTE);
            Log.e("Tag", Integer.toString(enceinte.getBondState()));
            if ((enceinte.getBondState() == BluetoothDevice.BOND_BONDED) && (bluetoothAdapter.getState() == BluetoothAdapter.STATE_ON)){
                TextView textView = (TextView)findViewById(R.id.enceinte_etat);
                textView.setText("oui");
                textView.setTextColor(Color.GREEN);
                return true;
            }
        }
        return false;
    }
}