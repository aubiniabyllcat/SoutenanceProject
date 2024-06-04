import '@/app/globals.css';
import Navbar from '@/components/landing-page/Navbar/index';
import Footer from '@/components/landing-page/Footer/Footer';


export const metadata = {
  title: 'SM',
  description: 'Generated by SM',
}


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
