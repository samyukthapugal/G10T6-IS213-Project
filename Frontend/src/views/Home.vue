<template>
  <div class="container-fluid p-0">
    <!-- Jumbotron for Introduction -->
    <div class="jumbotron jumbotron-fluid text-center text-white bg-dark mb-0">
      <div class="container">
        <h1 class="display-4">Welcome to Fitness World</h1>
        <p class="lead">Transform your life through fitness. Explore our diverse range of classes designed for all fitness levels.</p>
      </div>
    </div>

    <!-- Fitness Sections with Scroll -->
    <section>
	<div class="row">
		<div class="col-md-4 col-sm-6 col-xs-12">
			<div class="card">
				<div class="cover item-a">
					<h1>High Intensity<br>Interval Training</h1>
					
					<div class="card-back">
						<a class="text-white">Elevate your heart rate with our high-energy cardio classes.<br>Burn calories and boost your endurance!</a>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-4 col-sm-6 col-xs-12">
			<div class="card">
				<div class="cover item-b">
					<h1>Strength<br>Training</h1>
					
					<div class="card-back">
            <a class="text-white">Build lean muscle and sculpt your body with our effective strength training programs!</a>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-4 col-sm-6 col-xs-12">
			<div class="card">
				<div class="cover item-c">
					<h1>Yoga<br>Bliss</h1>
          <div class="card-back">
            <a class="text-white">Find balance and serenity with our yoga classes. Improve flexibility and reduce stress.</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

      <!-- Add more Fitness Sections as needed -->
<!-- * Call to Action Start * -->
<section class="section text-white" id="call-to-action">
        <div class="container">
            <div class="row">
                <div class="col-lg-10 offset-lg-1">
                    <div class="cta-content">
                        <h2>Don’t <em>think</em>, begin <em>today</em>!</h2>
                        <p>Get started on your fitness classes today!</p>
                        <div class="main-button scroll-to-section">
                            <a href="Register.vue">Register Now!</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- * Call to Action End * -->
  
  </div>
</template>
