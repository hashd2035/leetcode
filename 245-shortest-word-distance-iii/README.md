<h2><a href="https://leetcode.com/problems/shortest-word-distance-iii/">245. Shortest Word Distance III</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">wordsDict</code> and two strings that already exist in the array <code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code>, return <em style="user-select: auto;">the shortest distance between these two words in the list</em>.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Note</strong> that <code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code> may be the same. It is guaranteed that they represent <strong style="user-select: auto;">two individual words</strong> in the list.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
<strong style="user-select: auto;">Output:</strong> 1
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
<strong style="user-select: auto;">Output:</strong> 3
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordsDict.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordsDict[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">wordsDict[i]</code> consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code> are in <code style="user-select: auto;">wordsDict</code>.</li>
</ul>
</div>