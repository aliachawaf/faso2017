package fas.ig3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class RequeteHTTP {
    InputStream is = null;
    private String adresse_serveur;

    public RequeteHTTP(String adresse_serveur) {
        this.adresse_serveur = adresse_serveur;
    }

    public String doGET(String parametres) throws MalformedURLException, IOException {
        URL url = new URL("http://" + adresse_serveur + "/?" + parametres);
        HttpURLConnection httpUrlConnection = (HttpURLConnection) url.openConnection();
        httpUrlConnection.setReadTimeout(10000 /* milliseconds */);
        httpUrlConnection.setConnectTimeout(15000 /* milliseconds */);
        httpUrlConnection.setRequestMethod("GET");
        httpUrlConnection.setDoInput(true);
        httpUrlConnection.connect();
        is = httpUrlConnection.getInputStream();
        if (httpUrlConnection.getResponseCode() == HttpURLConnection.HTTP_OK) {
            String reponse = "None";
            reponse = readIt(is);
            httpUrlConnection.disconnect();
            System.out.println(reponse);
            return reponse;
        } else {
            httpUrlConnection.disconnect();
            throw new MalformedURLException();
        }
    }

    public String readIt(InputStream stream) throws IOException, UnsupportedEncodingException {
        StringBuilder builder = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
        String line;
        while ((line = reader.readLine()) != null) {
            builder.append(line);
        }
        return builder.toString();
    }

}

