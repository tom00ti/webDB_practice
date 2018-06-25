<!--ここでテンプレートを利用する事を低減-->
% rebase('templates/base.tpl')

<div>
	<h3> あなたの捕まえたアワビの特徴は？</h3>
</div>
<form action="/abalone" method="post">
	<fieldset>
		<legend align="left">入力フォーム</legend>
		<!--性別-->
		<div class="input-group fluid">
			<div class="col-sm-12 col-md-2">
				<label for="sex">性別</label>
			</div>
			<div class="col-sm-12 col-md">
				<select id="sex" name="sex">
					<option value="0">メス</option>
					<option value="1">不明</option>
					<option value="2">オス</option>
				</select>
			</div>
		</div>

		<!--数値入力（殻長:length）-->
		<div class="input-group fluid">
			<div class="col-sm-12 col-md-2">
				<label for="length">殻長</label>
			</div>
			<div class="col-sm-12 col-md">
				<input type="number" id="length" name="length" min="0" style="width: 20%;" required>
			</div>
		</div>

		<!--数値入力（殻長:diameter）-->
		<div class="input-group fluid">
			<div class="col-sm-12 col-md-2">
				<label for="diameter">殻幅</label>
			</div>
			<div class="col-sm-12 col-md">
				<input type="number" id="diameter" name="diameter" min="0" style="width: 20%;" required>
			</div>
		</div>

		<!--数値入力（殻長:height）-->
		<div class="input-group fluid">
			<div class="col-sm-12 col-md-2">
				<label for="height">高さ</label>
			</div>
			<div class="col-sm-12 col-md">
				<input type="number" id="height" name="height" min="0" style="width: 20%;" required>
			</div>
		</div>

		<!--数値入力（殻長:weight）-->
		<div class="input-group fluid">
			<div class="col-sm-12 col-md-2">
				<label for="weight">重さ</label>
			</div>
			<div class="col-sm-12 col-md">
				<input type="number" id="weight" name="weight" min="0" style="width: 20%;" required>
			</div>
		</div>

		<!--送信ボタン-->
		<div class="input-group">
			<input type="submit" class="primary" value="年齢を当てる">
		</div>
	</fieldset>
</form>h