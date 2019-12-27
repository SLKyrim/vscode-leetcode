

public class Test {

    public static void main(String[] args) {
        String tmp = "12 32";
        String[] arr = tmp.split("\\s+");
        int sum = 0;
        for (String ss : arr) {
            sum += Integer.parseInt(ss);
        }
        System.out.println(sum);
    }
}
