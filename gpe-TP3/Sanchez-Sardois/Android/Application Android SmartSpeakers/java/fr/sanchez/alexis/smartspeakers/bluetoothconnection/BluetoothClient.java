package fr.sanchez.alexis.smartspeakers.bluetoothconnection;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import java.io.IOException;
import java.io.OutputStream;
import java.util.UUID;

public class BluetoothClient {
    private final BluetoothSocket blClientSocket;
    private final BluetoothDevice blueDevice;
    private final BluetoothAdapter bluetoothAdapter;
    private final String UUID_APPLICATION = "69090025-0c61-4300-8330-7dcab0752d99";
    private OutputStream mmOutStream;
    private byte[] mmBuffer; // buffer
    private Handler mHandler;
    public static final int MESSAGE_TOAST = 2;


    public BluetoothClient(BluetoothDevice device) {
        BluetoothSocket tmp = null;
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        blueDevice = device;
        mmBuffer = new byte[1024];
        mHandler = new Handler();

        try {
            //On transforme notre chaine de caractère en UUID
            UUID uuid = UUID.fromString(UUID_APPLICATION);
            tmp = device.createRfcommSocketToServiceRecord(uuid);
        } catch (IOException e) {
        }
        blClientSocket = tmp;
        try {
            // On se connecte
            blClientSocket.connect();
        } catch (IOException connectException) {
            try {
                blClientSocket.close();
            } catch (IOException closeException) {
            }
            return;
        }

        try {
            this.mmOutStream = blClientSocket.getOutputStream();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Annule toute connexion en cours
    public void cancel() {
        try {
            blClientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void write(String msg) {
        try {
            //envoie des données par bluetooth
            byte[] bytes = msg.getBytes();
            mmOutStream.write(bytes);
        } catch (IOException e) {
            Log.e("Smart Speakers", "Erreur envoie des données impossible", e);

            // On envoie un msg d'erreur
            Message writeErrorMsg =
                    mHandler.obtainMessage(BluetoothClient.MESSAGE_TOAST);
            Bundle bundle = new Bundle();
            bundle.putString("toast",
                    "Erreur envoie données");
            writeErrorMsg.setData(bundle);
            mHandler.sendMessage(writeErrorMsg);
        }
    }
}

