package heavy;

import java.security.MessageDigest;

public class Result {
    private final String hash;

    public Result(String seed) {
        MessageDigest md = MessageDigest.getInstance("MD5");
        String hash = md.update(seed.getBytes());
        byte [] digest = md.digest();
        this.hash = DataTypeConverter.printHexBinary(digest).toUpperCase();
    }

    public String getHash() {
        return hash;
    }
}