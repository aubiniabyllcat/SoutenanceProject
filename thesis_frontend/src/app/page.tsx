import Scroll from './components/Scroll/index';
import Banner from './components/Banner/index';
import Features from './components/Administration/index';
import About from './components/About/index';
import Student from './components/Expert/index';
import Gallery from './components/Gallery/index';
import Newsletter from './components/Newsletter/Newsletter';



export default function Home() {
  return (
    <main>
      <Banner />
      <Features />
      <About />
      <Student />
      <Gallery />
      <Newsletter />
      <Scroll/>
    </main>
  )
}
