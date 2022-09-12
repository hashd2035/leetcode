<h2><a href="https://leetcode.com/problems/buildings-with-an-ocean-view/">1762. Buildings With an Ocean View</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are <code style="user-select: auto;">n</code> buildings in a line. You are given an integer array <code style="user-select: auto;">heights</code> of size <code style="user-select: auto;">n</code> that represents the heights of the buildings in the line.</p>

<p style="user-select: auto;">The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a <strong style="user-select: auto;">smaller</strong> height.</p>

<p style="user-select: auto;">Return a list of indices <strong style="user-select: auto;">(0-indexed)</strong> of buildings that have an ocean view, sorted in increasing order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [4,2,3,1]
<strong style="user-select: auto;">Output:</strong> [0,2,3]
<strong style="user-select: auto;">Explanation:</strong> Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [4,3,2,1]
<strong style="user-select: auto;">Output:</strong> [0,1,2,3]
<strong style="user-select: auto;">Explanation:</strong> All the buildings have an ocean view.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [1,3,2,4]
<strong style="user-select: auto;">Output:</strong> [3]
<strong style="user-select: auto;">Explanation:</strong> Only building 3 has an ocean view.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= heights.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= heights[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>