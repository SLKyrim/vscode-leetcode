import java.util.List;
import java.util.ArrayList;

class Solution {


    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        List<Integer> tmp1 = new ArrayList<>();
        List<Integer> tmp2 = new ArrayList<>();
        while (l1 != null) {
            tmp1.add(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            tmp2.add(l2.val);
            l2 = l2.next;
        }

        long sum1 = 0, sum2 = 0;
        for (int i = tmp1.size() - 1; i > -1; i--) {
            sum1 = sum1 * 10 + tmp1.get(i);
        }
        for (int i = tmp2.size() - 1; i > -1; i--) {
            sum2 = sum2 * 10 + tmp2.get(i);
        }

        long sum = sum1 + sum2;

        int firstNodeVal = (int) (sum % 10);
        ListNode List = new ListNode(firstNodeVal);
        ListNode res = List;
        sum = sum / 10;
        while (sum > 0) {
            int val = (int) (sum % 10);
            List.next = new ListNode(val);
            List = List.next;
            sum = sum / 10;
        }

        return res;
    }

    public static void main(String[] args) {
        ListNode tmp1 = new ListNode(1);
        ListNode tmp2 = new ListNode(1);
        ListNode l1 = tmp1;
        ListNode l2 = tmp2;
        for (int i = 0; i < 10; i++) {
            tmp1.next = new ListNode(1);
            tmp1 = tmp1.next;
            tmp2.next = new ListNode(1);
            tmp2 = tmp2.next;
        }

        ListNode res = addTwoNumbers(l1, l2);

        while (res != null) {
            System.out.print(res.val + " ");
            res = res.next;
        }

    }
}