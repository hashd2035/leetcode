<h2><a href="https://leetcode.com/problems/valid-word-abbreviation/">408. Valid Word Abbreviation</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A string can be <strong style="user-select: auto;">abbreviated</strong> by replacing any number of <strong style="user-select: auto;">non-adjacent</strong>, <strong style="user-select: auto;">non-empty</strong> substrings with their lengths. The lengths <strong style="user-select: auto;">should not</strong> have leading zeros.</p>

<p style="user-select: auto;">For example, a string such as <code style="user-select: auto;">"substitution"</code> could be abbreviated as (but not limited to):</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">"s10n"</code> (<code style="user-select: auto;">"s <u style="user-select: auto;">ubstitutio</u> n"</code>)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"sub4u4"</code> (<code style="user-select: auto;">"sub <u style="user-select: auto;">stit</u> u <u style="user-select: auto;">tion</u>"</code>)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"12"</code> (<code style="user-select: auto;">"<u style="user-select: auto;">substitution</u>"</code>)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"su3i1u2on"</code> (<code style="user-select: auto;">"su <u style="user-select: auto;">bst</u> i <u style="user-select: auto;">t</u> u <u style="user-select: auto;">ti</u> on"</code>)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"substitution"</code> (no substrings replaced)</li>
</ul>

<p style="user-select: auto;">The following are <strong style="user-select: auto;">not valid</strong> abbreviations:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">"s55n"</code> (<code style="user-select: auto;">"s <u style="user-select: auto;">ubsti</u> <u style="user-select: auto;">tutio</u> n"</code>, the replaced substrings are adjacent)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"s010n"</code> (has leading zeros)</li>
	<li style="user-select: auto;"><code style="user-select: auto;">"s0ubstitution"</code> (replaces an empty substring)</li>
</ul>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">word</code> and an abbreviation <code style="user-select: auto;">abbr</code>, return <em style="user-select: auto;">whether the string <strong style="user-select: auto;">matches</strong> the given abbreviation</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">substring</strong> is a contiguous <strong style="user-select: auto;">non-empty</strong> sequence of characters within a string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> word = "internationalization", abbr = "i12iz4n"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The word "internationalization" can be abbreviated as "i12iz4n" ("i <u style="user-select: auto;">nternational</u> iz <u style="user-select: auto;">atio</u> n").
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> word = "apple", abbr = "a2e"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The word "apple" cannot be abbreviated as "a2e".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word.length &lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">word</code> consists of only lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= abbr.length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">abbr</code> consists of lowercase English letters and digits.</li>
	<li style="user-select: auto;">All the integers in <code style="user-select: auto;">abbr</code> will fit in a 32-bit integer.</li>
</ul>
</div>