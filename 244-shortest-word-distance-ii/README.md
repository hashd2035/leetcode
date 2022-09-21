<h2><a href="https://leetcode.com/problems/shortest-word-distance-ii/">244. Shortest Word Distance II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">WordDistance</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">WordDistance(String[] wordsDict)</code> initializes the object with the strings array <code style="user-select: auto;">wordsDict</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int shortest(String word1, String word2)</code> returns the shortest distance between <code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code> in the array <code style="user-select: auto;">wordsDict</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
<strong style="user-select: auto;">Output</strong>
[null, 3, 1]

<strong style="user-select: auto;">Explanation</strong>
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordsDict.length &lt;= 3 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordsDict[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">wordsDict[i]</code> consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code> are in <code style="user-select: auto;">wordsDict</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word1 != word2</code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">5000</code> calls will be made to <code style="user-select: auto;">shortest</code>.</li>
</ul>
</div>