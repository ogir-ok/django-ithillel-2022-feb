<template>
  <div class="row">
    <button class="btn btn-primary" @click="fetchMovies(nextLink)">Next</button>
  </div>
  <div class="row">
  <div class="col" v-for="movie in movies">
    <a :href="`/movie/${movie.id}/`">
      <div class="card" style="width: 18rem;">
        <img src="..." class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{{movie.name}}</h5>
          <p>{{ movie.director }}</p>
          <p class="card-text"><span class="badge rounded-pill"> Horror</span> </p>
        </div>
    </div>
    </a>
  </div>
  </div>

</template>

<script>
export default {
  name: "MoviesList",
  data() {
    return {
      movies: [],
      nextLink: null,
      previousLink: null,
      pageNo: null
    }
  },
  async mounted() {
    await this.fetchMovies()
  },
  methods: {
    async fetchMovies(url) {
      const targetUrl = url ? url : '/api/imdb/'
      const res = await fetch(targetUrl)
      const data = await res.json()
      this.movies = data["results"];
      this.nextLink = data["next"]
      this.previousLink = data["previous"]
    },
    async addMovie(url) {
      await fetch('/api/imdb/', {
        'method': 'POST',
        'data': {

        }
      } )
    }
  }
}
</script>

<style scoped>

</style>
