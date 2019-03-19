package heavy;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.xml.bind.DatatypeConverter;

public class Result {
    private final String hash;

    public Result(String seed) {
        String hash;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(seed.getBytes());
            byte[] digest = md.digest();
            hash = DatatypeConverter.printHexBinary(digest).toUpperCase();
        } catch (NoSuchAlgorithmException nsae) {
            hash = "";
        }
        this.hash = hash;
    }

    public String getHash() {
        return this.hash;
    }
}