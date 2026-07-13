class Solution {
    public String oddString(String[] words) {

        int count_1 = 0;
        int count_2 = 0;
        int val_1 = -1;
        int val_2 = -1;
        int index_1 = -1;
        int index_2 = -1;


        for (int i = 0; i < words.length; i++) {
            int temp_val = 0;
            int mul = 1;

            for (int j = 0; j < words[i].length() - 1; j++) {
                temp_val += mul * ((words[i].charAt(j+1) - 'a') - (words[i].charAt(j)) - 'a');
                mul *= 10;
            }

            if (count_1 == 0) {
                val_1 = temp_val;
                count_1 += 1;
                index_1 = i;
            } else {
                if (val_1 == temp_val) {
                    val_1 = temp_val;
                    count_1 += 1;
                    index_1 = i;
                } else {
                    val_2 = temp_val;
                    count_2 += 1;
                    index_2 = i;
                }
            }

        }


        if (count_1 == 1) {
            return words[index_1];
        }
        return words[index_2];
    }
}
