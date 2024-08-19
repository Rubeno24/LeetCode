class Leetcode1732 {
  public int largestAltitude(int[] gain) {
    // 2 vairbales one that holds the sum and one that holds the tallest alt
    int sum = 0;
    int tallest = 0;
    // for loop to move through the array
    for (int i = 0; i < gain.length; i++) {
      // store the sum of the array at i
      sum += gain[i];
      // then check if sum is greater then tallest, if so set tallest = sum
      if (sum > tallest) {
        tallest = sum;
      }

    }
    // return the tallest variable
    return tallest;

  }

}
