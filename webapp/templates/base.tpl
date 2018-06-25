<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>アワビ！</title>
	<link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v2.3.7/dist/mini-default.min.css">

	% setdefault('use_bokeh',False)
	% if use_bokeh:
		<link rel="stylesheet" type="text/css" href="http://cdn.pydata.org/bokh/release/bokh-0.13.0.min.css">>
		<script src="http://cdn.pydata.org/bokh/release/bokh-0.13.0.min.js" ></script>
		{{!script}}
	%end

	<meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body>
	<header>
		<a href="/" class="button">
			アワビの年齢推定アプリケーション
		</a>
	</header>

	<!--別のテンプレートで置き換える-->
	{{ !base }}

</body>
</html>