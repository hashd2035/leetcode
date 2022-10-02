<h2><a href="https://leetcode.com/problems/two-sum-less-than-k/">1099. Two Sum Less Than K</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">nums</code> of integers and&nbsp;integer <code style="user-select: auto;">k</code>, return the maximum <code style="user-select: auto;">sum</code> such that there exists <code style="user-select: auto;">i &lt; j</code> with <code style="user-select: auto;">nums[i] + nums[j] = sum</code> and <code style="user-select: auto;">sum &lt; k</code>. If no <code style="user-select: auto;">i</code>, <code style="user-select: auto;">j</code> exist satisfying this equation, return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [34,23,1,24,75,33,54,8], k = 60
<strong style="user-select: auto;">Output:</strong> 58
<strong style="user-select: auto;">Explanation: </strong>We can use 34 and 24 to sum 58 which is less than 60.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [10,20,30], k = 15
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation: </strong>In this case it is not possible to get a pair sum less that 15.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 2000</code></li>
</ul>
</div>