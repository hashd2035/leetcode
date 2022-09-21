<h2><a href="https://leetcode.com/problems/shortest-word-distance/">243. Shortest Word Distance</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">wordsDict</code> and two different strings that already exist in the array <code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code>, return <em style="user-select: auto;">the shortest distance between these two words in the list</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= wordsDict.length &lt;= 3 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordsDict[i].length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">wordsDict[i]</code> consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word1</code> and <code style="user-select: auto;">word2</code> are in <code style="user-select: auto;">wordsDict</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">word1 != word2</code></li>
</ul>
</div>